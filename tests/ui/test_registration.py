import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.attach import add_screenshot


@allure.feature('UI Tests')
@allure.story('SauceDemo')
class TestSauceDemo:

    BASE_URL = "https://www.saucedemo.com"

    def _login(self, driver, username="standard_user", password="secret_sauce"):
        """Вспомогательный метод для логина"""
        driver.get(self.BASE_URL)
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

    @allure.title("Successful login")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_successful_login(self, driver):
        with allure.step('Open login page'):
            driver.get(self.BASE_URL)

        with allure.step('Enter credentials'):
            driver.find_element(By.ID, "user-name").send_keys("standard_user")
            driver.find_element(By.ID, "password").send_keys("secret_sauce")

        with allure.step('Click login'):
            driver.find_element(By.ID, "login-button").click()

        with allure.step('Verify login success'):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "title"))
            )
            assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
            add_screenshot(driver, "Login success")

    @allure.title("Login with invalid password")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_login_invalid_password(self, driver):
        with allure.step('Open login page'):
            driver.get(self.BASE_URL)

        with allure.step('Enter wrong password'):
            driver.find_element(By.ID, "user-name").send_keys("standard_user")
            driver.find_element(By.ID, "password").send_keys("wrong_password")

        with allure.step('Click login'):
            driver.find_element(By.ID, "login-button").click()

        with allure.step('Verify error message'):
            error = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
            )
            assert "Username and password do not match" in error.text

    @allure.title("Sort products by price")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_sort_by_price(self, driver):
        with allure.step('Login'):
            self._login(driver)

        with allure.step('Sort by price high to low'):
            sort = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product_sort_container"))
            )
            sort.click()
            driver.find_element(By.CSS_SELECTOR, "option[value='hilo']").click()

        with allure.step('Verify sorting'):
            prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
            price_values = [float(p.text.replace('$', '')) for p in prices]
            assert price_values == sorted(price_values, reverse=True)
            add_screenshot(driver, "Sorted by price")

    @allure.title("Add product to cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_add_to_cart(self, driver):
        with allure.step('Login'):
            self._login(driver)

        with allure.step('Add first product to cart'):
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_inventory"))
            ).click()

        with allure.step('Verify cart badge'):
            badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            assert badge.text == "1"
            add_screenshot(driver, "Product added to cart")

    @allure.title("Checkout flow")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_checkout(self, driver):
        with allure.step('Login and add product'):
            self._login(driver)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_inventory"))
            ).click()

        with allure.step('Go to cart'):
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        with allure.step('Click checkout'):
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            ).click()

        with allure.step('Fill checkout info'):
            driver.find_element(By.ID, "first-name").send_keys("John")
            driver.find_element(By.ID, "last-name").send_keys("Doe")
            driver.find_element(By.ID, "postal-code").send_keys("12345")

        with allure.step('Continue and finish'):
            driver.find_element(By.ID, "continue").click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "finish"))
            ).click()

        with allure.step('Verify success message'):
            header = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
            )
            assert "Thank you for your order!" in header.text
            add_screenshot(driver, "Checkout complete")