# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # Selenoid настройки
    SELENOID_URL = os.getenv('SELENOID_URL', 'selenoid.autotests.cloud/wd/hub')
    SELENOID_USER = os.getenv('SELENOID_USER', '')
    SELENOID_PASSWORD = os.getenv('SELENOID_PASSWORD', '')

    # URL тестовых приложений
    BASE_URL = os.getenv('BASE_URL', 'https://www.saucedemo.com')
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://reqres.in/api')
    SAUCEDEMO_URL = os.getenv('SAUCEDEMO_URL', 'https://www.saucedemo.com')
    JSONPLACEHOLDER_URL = os.getenv('JSONPLACEHOLDER_URL', 'https://jsonplaceholder.typicode.com')

    # Настройки браузера
    BROWSER = os.getenv('BROWSER', 'chrome')
    BROWSER_VERSION = os.getenv('BROWSER_VERSION', '128.0')
    WINDOW_WIDTH, WINDOW_HEIGHT = map(int, os.getenv('WINDOW_SIZE', '1920,1080').split(','))
    TIMEOUT = int(os.getenv('TIMEOUT', '30'))

    # Telegram уведомления
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')

    # Allure настройки
    ALLURE_MAX_ATTACHMENT_SIZE = int(os.getenv('ALLURE_MAX_ATTACHMENT_SIZE', '5000'))

    # Selenoid видео
    SELENOID_VIDEO_URL = os.getenv('SELENOID_VIDEO_URL', 'https://selenoid.autotests.cloud/video')
    VIDEO_DOWNLOAD_TIMEOUT = int(os.getenv('VIDEO_DOWNLOAD_TIMEOUT', '30'))  # ← добавить эту строку


settings = Settings()