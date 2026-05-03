import allure
from allure_commons.types import AttachmentType


def add_screenshot(driver, name='screenshot'):
    png = driver.get_screenshot_as_png()
    allure.attach(body=png, name=name, attachment_type=AttachmentType.PNG, extension='.png')


def add_console_logs(driver, name='browser_logs'):
    try:
        log = "".join(f'{text}\n' for text in driver.execute("getLog", {'type': 'browser'})['value'])
        allure.attach(log, name, AttachmentType.TEXT, '.log')
    except Exception:
        allure.attach("No console logs available", name, AttachmentType.TEXT, '.log')


def add_page_source(driver, name='page_source'):
    html = driver.page_source
    allure.attach(html, name, AttachmentType.HTML, '.html')


def add_video(driver, name=None):
    session_id = driver.session_id
    video_url = f"https://ru.selenoid.autotests.cloud/video/{session_id}.mp4"
    video_name = name if name else f'video_{session_id}'
    html = f"""<html><body><video width='100%' height='100%' controls autoplay>
    <source src='{video_url}' type='video/mp4'>
    </video></body></html>"""
    allure.attach(html, video_name, AttachmentType.HTML, '.html')