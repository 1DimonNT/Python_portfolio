# pages/login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.products_page import ProductsPage
from config.settings import settings


class LoginPage(BasePage):
    """Страница логина SauceDemo"""

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = settings.SAUCEDEMO_URL  # ← теперь берем из настроек

    def open(self):
        """Открыть страницу логина"""
        super().open(self.url)
        return self

    def login(self, username: str, password: str) -> ProductsPage:
        """Выполнить логин и вернуть страницу продуктов"""
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return ProductsPage(self.driver)

    def login_expecting_error(self, username: str, password: str) -> str:
        """Попытаться залогиниться и вернуть текст ошибки"""
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self.get_error_text()

    def get_error_text(self) -> str:
        """Получить текст сообщения об ошибке"""
        return self.get_text(self.ERROR_MESSAGE)

    def is_login_button_visible(self) -> bool:
        """Проверить, видна ли кнопка логина"""
        return self.is_visible(self.LOGIN_BUTTON)