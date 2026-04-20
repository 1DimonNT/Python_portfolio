import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.attach import add_screenshot, add_console_logs


@allure.feature('UI Tests')
@allure.story('SauceDemo Login')
class TestSauceDemo:

    BASE_URL = "https://www.saucedemo.com"

    @allure.title("Successful login to SauceDemo")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_successful_login(self, driver):
        with allure.step('Open SauceDemo login page'):
            driver.get(self.BASE_URL)
            add_screenshot(driver, "📸 1. Login page opened")
            add_console_logs(driver, "Console logs after open")

        with allure.step('Enter username "standard_user"'):
            username_input = driver.find_element(By.ID, "user-name")
            username_input.send_keys("standard_user")
            add_screenshot(driver, "📸 2. Username entered")

        with allure.step('Enter password "secret_sauce"'):
            password_input = driver.find_element(By.ID, "password")
            password_input.send_keys("secret_sauce")
            add_screenshot(driver, "📸 3. Password entered")

        with allure.step('Click login button'):
            login_button = driver.find_element(By.ID, "login-button")
            login_button.click()
            add_screenshot(driver, "📸 4. Login button clicked")

        with allure.step('Verify successful login - products page is displayed'):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "title"))
            )
            title = driver.find_element(By.CLASS_NAME, "title").text
            assert title == "Products"
            add_screenshot(driver, "📸 5. Products page verified - SUCCESS")

            @allure.title("Test that fails to check screenshot")
            def test_fail_screenshot(driver):
                driver.get("https://demoqa.com")
                # Этот тест упадёт, потому что элемента нет
                driver.find_element(By.ID, "non_existent_element").click()