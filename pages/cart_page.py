# pages/cart_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage


class CartPage(BasePage):
    """Страница корзины SauceDemo"""

    # Locators
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, ".cart_button")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CART_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def checkout(self) -> CheckoutPage:
        """Нажать кнопку Checkout"""
        self.click(self.CHECKOUT_BUTTON)
        return CheckoutPage(self.driver)

    def get_cart_items_count(self) -> int:
        """Получить количество товаров в корзине"""
        return len(self.get_elements(self.CART_ITEM))

    def remove_item_by_index(self, index: int):
        """Удалить товар из корзины по индексу"""
        remove_buttons = self.get_elements(self.REMOVE_BUTTONS)
        if index < len(remove_buttons):
            remove_buttons[index].click()
        return self

    def continue_shopping(self):
        """Вернуться к покупкам"""
        from pages.products_page import ProductsPage  # ✅ импорт внутри метода
        self.click(self.CONTINUE_SHOPPING_BUTTON)
        return ProductsPage(self.driver)