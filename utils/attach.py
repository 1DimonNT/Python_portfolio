# utils/attach.py
import allure
from allure_commons.types import AttachmentType
import requests
import time
from config.settings import settings


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
    """Добавить видео из Selenoid в отчет Allure"""
    time.sleep(3)

    # Используем имя сессии или переданное имя
    video_name = name if name else driver.session_id
    video_url = f"{settings.SELENOID_VIDEO_URL}/{video_name}.mp4"

    try:
        response = requests.get(video_url, timeout=settings.VIDEO_DOWNLOAD_TIMEOUT)
        if response.status_code == 200 and len(response.content) > 10000:
            allure.attach(
                body=response.content,
                name=video_name,
                attachment_type=AttachmentType.MP4,
                extension='.mp4'
            )
        else:
            allure.attach(
                f"Видео не найдено: {video_url} (status: {response.status_code})",
                name="video_error",
                attachment_type=AttachmentType.TEXT
            )
    except Exception as e:
        allure.attach(
            f"Ошибка при загрузке видео: {str(e)}",
            name="video_error",
            attachment_type=AttachmentType.TEXT
        )