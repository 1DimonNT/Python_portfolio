# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple, Optional, List


class BasePage:
    """Базовый класс для всех Page Objects"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url: str):
        """Открыть URL"""
        self.driver.get(url)
        return self

    def click(self, locator: Tuple[str, str]):
        """Кликнуть по элементу с ожиданием кликабельности"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

    def input_text(self, locator: Tuple[str, str], text: str):
        """Ввести текст в поле"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        return self

    def get_text(self, locator: Tuple[str, str]) -> str:
        """Получить текст элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator: Tuple[str, str]) -> bool:
        """Проверить, видим ли элемент"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def get_elements(self, locator: Tuple[str, str]) -> List[WebElement]:
        """Получить все элементы по локатору"""
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def wait_for_url_contains(self, partial_url: str):
        """Дождаться, когда URL содержит подстроку"""
        self.wait.until(EC.url_contains(partial_url))
        return self

    def scroll_to_element(self, locator: Tuple[str, str]):
        """Прокрутить до элемента"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return self