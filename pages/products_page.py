# pages/products_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from typing import List


class ProductsPage(BasePage):
    """Страница со списком товаров SauceDemo"""

    # Locators
    TITLE = (By.CLASS_NAME, "title")
    PRODUCT_SORT = (By.CLASS_NAME, "product_sort_container")
    SORT_HIGH_TO_LOW = (By.CSS_SELECTOR, "option[value='hilo']")
    SORT_LOW_TO_HIGH = (By.CSS_SELECTOR, "option[value='lohi']")
    SORT_NAME_A_TO_Z = (By.CSS_SELECTOR, "option[value='az']")
    SORT_NAME_Z_TO_A = (By.CSS_SELECTOR, "option[value='za']")

    # Рабочие локаторы
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, ".btn_inventory")
    FIRST_ADD_TO_CART = (By.CSS_SELECTOR, ".btn_inventory")

    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_title(self) -> str:
        """Получить заголовок страницы"""
        return self.get_text(self.TITLE)

    def sort_by_price_high_to_low(self):
        """Отсортировать товары по цене (дорогие сверху)"""
        self.click(self.PRODUCT_SORT)
        self.click(self.SORT_HIGH_TO_LOW)
        return self

    def sort_by_price_low_to_high(self):
        """Отсортировать товары по цене (дешевые сверху)"""
        self.click(self.PRODUCT_SORT)
        self.click(self.SORT_LOW_TO_HIGH)
        return self

    def sort_by_name_a_to_z(self):
        """Отсортировать товары по имени (А→Я)"""
        self.click(self.PRODUCT_SORT)
        self.click(self.SORT_NAME_A_TO_Z)
        return self

    def sort_by_name_z_to_a(self):
        """Отсортировать товары по имени (Я→А)"""
        self.click(self.PRODUCT_SORT)
        self.click(self.SORT_NAME_Z_TO_A)
        return self

    def get_product_prices(self) -> List[float]:
        """Получить список цен всех товаров"""
        price_elements = self.get_elements(self.PRODUCT_PRICES)
        return [float(p.text.replace('$', '')) for p in price_elements]

    def add_first_product_to_cart(self):
        """Добавить первый товар в корзину"""
        # Ждем, когда появится хотя бы одна кнопка
        self.wait.until(lambda d: len(d.find_elements(*self.ADD_TO_CART_BUTTONS)) > 0)
        # Кликаем по первой
        self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)[0].click()
        return self

    def add_product_to_cart_by_index(self, index: int):
        """Добавить товар по индексу в корзину"""
        # Ждем, когда появятся кнопки
        self.wait.until(lambda d: len(d.find_elements(*self.ADD_TO_CART_BUTTONS)) > index)
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        if index < len(buttons):
            buttons[index].click()
        return self

    def get_cart_count(self) -> int:
        """Получить количество товаров в корзине"""
        if self.is_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def go_to_cart(self):
        """Перейти в корзину"""
        from pages.cart_page import CartPage
        self.click(self.CART_ICON)
        return CartPage(self.driver)