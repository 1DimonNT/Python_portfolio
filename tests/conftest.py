import os
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import settings
from utils import attach


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='Browser to run tests')


@pytest.fixture(scope='function')
def driver(request):
    options = Options()
    options.add_argument(f'--window-size={settings.WINDOW_WIDTH},{settings.WINDOW_HEIGHT}')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Включаем запись видео для Selenoid
    if 'SELENOID_URL' in os.environ:
        capabilities = {
            "browserName": settings.BROWSER,
            "browserVersion": settings.BROWSER_VERSION,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True,
                "videoName": f"{request.node.name}.mp4"
            }
        }
        options.capabilities.update(capabilities)
        selenoid_url = f'https://{settings.SELENOID_USER}:{settings.SELENOID_PASSWORD}@{settings.SELENOID_URL}'
        driver = webdriver.Remote(command_executor=selenoid_url, options=options)
        print(f"✅ Running on Selenoid: {selenoid_url}")
    else:
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        print("✅ Running locally with ChromeDriver")

    driver.implicitly_wait(settings.TIMEOUT)
    request.node.driver = driver
    yield driver

    # Вложения ПОСЛЕ теста
    attach.add_screenshot(driver, '📸 FINAL - End of test')
    attach.add_page_source(driver)
    attach.add_console_logs(driver)

    # Видео только для Selenoid
    if 'SELENOID_URL' in os.environ:
        attach.add_video(driver)

    driver.quit()


# ============= АВТОМАТИЧЕСКИЕ СКРИНШОТЫ ПРИ ПАДЕНИИ ТЕСТА =============

def add_screenshot_on_failure(driver, name='screenshot'):
    """Делает скриншот и прикрепляет к Allure"""
    png = driver.get_screenshot_as_png()
    allure.attach(body=png, name=name, attachment_type=AttachmentType.PNG, extension='.png')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Проверяем, что тест упал именно во время выполнения
    if rep.when == 'call' and rep.failed:
        # Пытаемся найти драйвер
        if hasattr(item, 'driver'):
            driver = item.driver
            # Делаем скриншот с именем теста
            add_screenshot_on_failure(driver, name=f"❌ FAILURE - {item.name}")
            print(f"📸 Скриншот сделан для упавшего теста: {item.name}")
        else:
            print("⚠️ Драйвер не найден, скриншот не сделан")