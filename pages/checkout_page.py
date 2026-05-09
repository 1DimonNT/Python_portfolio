# pages/checkout_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from typing import Dict


class CheckoutPage(BasePage):
    """Страница оформления заказа SauceDemo"""

    # Locators
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    ITEM_TOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_LABEL = (By.CLASS_NAME, "summary_tax_label")

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        """Заполнить информацию о покупателе"""
        self.input_text(self.FIRST_NAME_INPUT, first_name)
        self.input_text(self.LAST_NAME_INPUT, last_name)
        self.input_text(self.POSTAL_CODE_INPUT, postal_code)
        return self

    def continue_to_overview(self):
        """Нажать Continue"""
        self.click(self.CONTINUE_BUTTON)
        return self

    def finish_order(self):
        """Нажать Finish для завершения заказа"""
        self.click(self.FINISH_BUTTON)
        return self

    def get_complete_message(self) -> str:
        """Получить сообщение об успешном заказе"""
        return self.get_text(self.COMPLETE_HEADER)

    def get_total_amount(self) -> float:
        """Получить итоговую сумму"""
        total_text = self.get_text(self.TOTAL_LABEL)
        return float(total_text.replace('Total: $', ''))

    def cancel_order(self):
        """Отменить оформление заказа"""
        self.click(self.CANCEL_BUTTON)
        return self

    def complete_checkout_flow(self, first_name: str, last_name: str, postal_code: str):
        """Полный флоу оформления заказа в одном методе"""
        return (self.fill_checkout_info(first_name, last_name, postal_code)
                .continue_to_overview()
                .finish_order())