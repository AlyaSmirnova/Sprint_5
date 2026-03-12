import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import StellarBurgersLocators
from src.data import Data


@allure.suite('User Authentication Tests')
@allure.feature('Logout Functionality')
class TestStellarBurgersLogoutFromPersonalAccount:

    @allure.title('Logout from Personal Account')
    @allure.description('Verify that user can successfully log out from the personal account section')
    def test_logout_from_personal_account(self, driver):
        with allure.step('Authorize with valid credentials'):
            driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN_BUTTON).click()
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_BUTTON))
            driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(Data.LOGIN)
            driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
            driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        with allure.step('Navigate to Personal Account'):
            account_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON))
            try:
                WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains("/account"))
            except:
                driver.execute_script("arguments[0].click();", account_button)
                WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains("/account"))
        with allure.step('Click Logout button'):
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGOUT_BUTTON)).click()
        with allure.step('Verify redirection to Login page'):
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGIN_HEADER))
            assert '/login' in driver.current_url, 'Redirection to login page failed after logout'
