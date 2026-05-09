# tests/ui/test_saucedemo.py
import pytest
import allure
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature('UI Tests')
@allure.story('SauceDemo')
class TestSauceDemo:

    @allure.title("Successful login")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_successful_login(self, driver):
        login_page = LoginPage(driver)
        products_page = login_page.open().login("standard_user", "secret_sauce")

        assert products_page.get_title() == "Products"

    @allure.title("Login with invalid password")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_login_invalid_password(self, driver):
        login_page = LoginPage(driver)
        error_text = login_page.open().login_expecting_error("standard_user", "wrong_password")

        assert "Username and password do not match" in error_text

    @allure.title("Sort products by price")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_sort_by_price(self, driver):
        products_page = (LoginPage(driver)
                         .open()
                         .login("standard_user", "secret_sauce")
                         .sort_by_price_high_to_low())

        prices = products_page.get_product_prices()
        assert prices == sorted(prices, reverse=True)

    @allure.title("Add product to cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_add_to_cart(self, driver):
        cart_count = (LoginPage(driver)
                      .open()
                      .login("standard_user", "secret_sauce")
                      .add_first_product_to_cart()
                      .get_cart_count())

        assert cart_count == 1

    @allure.title("Checkout flow")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_checkout(self, driver):
        complete_message = (LoginPage(driver)
                            .open()
                            .login("standard_user", "secret_sauce")
                            .add_first_product_to_cart()
                            .go_to_cart()
                            .checkout()
                            .fill_checkout_info("John", "Doe", "12345")
                            .continue_to_overview()
                            .finish_order()
                            .get_complete_message())

        assert "Thank you for your order" in complete_message

    @allure.title("Verify cart badge counter")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_cart_badge_counter(self, driver):
        products_page = (LoginPage(driver)
                         .open()
                         .login("standard_user", "secret_sauce"))

        products_page.add_product_to_cart_by_index(0)
        assert products_page.get_cart_count() == 1

        products_page.add_product_to_cart_by_index(1)
        assert products_page.get_cart_count() == 2

        cart_page = products_page.go_to_cart()
        assert cart_page.get_cart_items_count() == 2

    @allure.title("Complete checkout with minimal data")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_checkout_with_minimal_data(self, driver):
        checkout_page = (LoginPage(driver)
                         .open()
                         .login("standard_user", "secret_sauce")
                         .add_first_product_to_cart()
                         .go_to_cart()
                         .checkout())

        complete_message = (checkout_page
                            .complete_checkout_flow("Jane", "Smith", "67890")
                            .get_complete_message())

        assert "Thank you for your order" in complete_message