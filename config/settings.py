import os 
from dotenv import load_dotenv 

load_dotenv()

class Settings:
    SELENOID_URL = os.getenv('SELENOID_URL', 'selenoid.autotests.cloud/wd/hub')
    SELENOID_USER = os.getenv('SELENOID_USER', '')
    SELENOID_PASSWORD = os.getenv('SELENOID_PASSWORD', '')
    BASE_URL = os.getenv('BASE_URL', 'https://demoqa.com')
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://reqres.in/api')
    BROWSER = os.getenv('BROWSER', 'chrome')
    BROWSER_VERSION = os.getenv('BROWSER_VERSION', '128.0')
    WINDOW_WIDTH, WINDOW_HEIGHT = map(int, os.getenv('WINDOW_SIZE', '1920,1080').split(','))
    TIMEOUT = int(os.getenv('TIMEOUT', '30'))
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')

settings = Settings()