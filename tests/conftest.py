import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import settings
from utils import attach


@pytest.fixture(scope='function')
def driver(request):
    options = Options()
    options.add_argument(f'--window-size={settings.WINDOW_WIDTH},{settings.WINDOW_HEIGHT}')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    if 'SELENOID_URL' in os.environ:
        selenoid_host = settings.SELENOID_URL.replace('https://', '').replace('http://', '').rstrip('/')
        selenoid_url = f'https://{settings.SELENOID_USER}:{settings.SELENOID_PASSWORD}@{selenoid_host}'

        options.set_capability("browserName", settings.BROWSER)
        options.set_capability("browserVersion", settings.BROWSER_VERSION)
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": True,
            "videoName": f"{request.node.name}.mp4",
            "videoScreenSize": f"{settings.WINDOW_WIDTH}x{settings.WINDOW_HEIGHT}"
        })

        driver = webdriver.Remote(command_executor=selenoid_url, options=options)
    else:
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(settings.TIMEOUT)
    request.node.driver = driver
    yield driver

    attach.add_screenshot(driver)
    attach.add_page_source(driver)
    attach.add_console_logs(driver)

    if 'SELENOID_URL' in os.environ:
        attach.add_video(driver)

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call' and rep.failed:
        if hasattr(item, 'driver'):
            attach.add_screenshot(item.driver, name=f"❌ FAILURE - {item.name}")