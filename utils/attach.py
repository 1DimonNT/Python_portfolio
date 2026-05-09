import allure
from allure_commons.types import AttachmentType
import requests
import time


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
    # Нужно дождаться, пока Selenoid обработает видео
    time.sleep(2)

    if name:
        video_url = f"https://selenoid.autotests.cloud/video/{name}.mp4"
    else:
        video_url = f"https://selenoid.autotests.cloud/video/{driver.session_id}.mp4"

    try:
        response = requests.get(video_url, timeout=30)
        if response.status_code == 200:
            allure.attach(
                body=response.content,
                name=name if name else f"video_{driver.session_id}",
                attachment_type=AttachmentType.MP4,
                extension='.mp4'
            )
        else:
            # fallback: прикрепляем ссылку текстом, если видео недоступно
            allure.attach(
                f"Видео не найдено по ссылке: {video_url}",
                name="video_error",
                attachment_type=AttachmentType.TEXT
            )
    except Exception as e:
        allure.attach(
            f"Ошибка при скачивании видео: {str(e)}",
            name="video_error",
            attachment_type=AttachmentType.TEXT
        )