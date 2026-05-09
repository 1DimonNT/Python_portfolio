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

    # Пробуем найти видео по имени теста
    video_name = name if name else driver.session_id

    # Вариант 1: по имени теста
    video_url_by_name = f"{settings.SELENOID_VIDEO_URL}/{video_name}.mp4"

    # Вариант 2: по session_id (более надежно)
    video_url_by_session = f"{settings.SELENOID_VIDEO_URL}/{driver.session_id}.mp4"

    video_found = False

    # Сначала пробуем по имени теста
    try:
        response = requests.get(video_url_by_name, timeout=settings.VIDEO_DOWNLOAD_TIMEOUT)
        if response.status_code == 200 and len(response.content) > 10000:
            allure.attach(
                body=response.content,
                name=f"video_{video_name}",
                attachment_type=AttachmentType.MP4,
                extension='.mp4'
            )
            video_found = True
    except Exception:
        pass

    # Если не нашли - пробуем по session_id
    if not video_found:
        try:
            response = requests.get(video_url_by_session, timeout=settings.VIDEO_DOWNLOAD_TIMEOUT)
            if response.status_code == 200 and len(response.content) > 10000:
                allure.attach(
                    body=response.content,
                    name=f"video_{driver.session_id}",
                    attachment_type=AttachmentType.MP4,
                    extension='.mp4'
                )
                video_found = True
        except Exception:
            pass

    # Если видео нет - пишем информативное сообщение (не ошибку)
    if not video_found:
        allure.attach(
            f"ℹ️ Видео не найдено для теста '{video_name}'\n"
            f"Session ID: {driver.session_id}\n"
            f"Проверенные URL:\n"
            f"  - {video_url_by_name}\n"
            f"  - {video_url_by_session}\n\n"
            f"Возможные причины:\n"
            f"  - Тест завершился слишком быстро\n"
            f"  - Проблема на стороне Selenoid\n"
            f"  - Видео еще не сгенерировано",
            name="video_not_available",
            attachment_type=AttachmentType.TEXT
        )