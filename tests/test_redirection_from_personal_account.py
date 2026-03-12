import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import StellarBurgersLocators
from src.data import Data


@allure.suite('Navigation Tests')
@allure.feature('Navigation from Personal Account')
class TestStellarBurgersRedirectionFromPersonalAccount:

    @allure.title('Redirect to Constructor via "Constructor" button')
    @allure.description('Verify that user can navigate back to the main page from the account section using the Constructor button')
    def test_redirection_from_personal_account_through_constructor_button(self, driver):
        with allure.step('Log in to the system'):
            driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN_BUTTON).click()
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_BUTTON))
            driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(Data.LOGIN)
            driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
            driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        with allure.step('Go to Personal Account and wait for profile page'):
            account_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON))
            try:
                WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains("/account"))
            except:
                driver.execute_script("arguments[0].click();", account_button)
                WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains("/account"))
        with allure.step('Click "Constructor" button in the header'):
            constructor_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.CONSTRUCTOR_BUTTON))
            constructor_button.click()
        with allure.step('Verify redirection to the main page (Constructor)'):
            make_an_order_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.MAKE_AN_ORDER_BUTTON))
            assert make_an_order_button.is_displayed(), 'Failed to redirect to Constructor page'

    @allure.title('Redirect to Main Page via Stellar Burgers Logo')
    @allure.description('Verify that clicking the logo redirects the user back to the main page from the account section')
    def test_redirection_from_personal_account_trough_logo(self, driver):
        with allure.step('Log in to the system'):
            driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN_BUTTON).click()
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_BUTTON))
            driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(Data.LOGIN)
            driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
            driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        with allure.step('Go to Personal Account'):
            account_button = WebDriverWait(driver, Config.TIMEOUT).until(
                expected_conditions.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON))
            try:
                WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains("/account"))
            except:
                driver.execute_script("arguments[0].click();", account_button)
                WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains("/account"))
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains("/account"))
        with allure.step('Click on the Stellar Burgers logo'):
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGO)).click()
        with allure.step('Verify redirection to the main page'):
            make_an_order_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.MAKE_AN_ORDER_BUTTON))
            assert make_an_order_button.is_displayed(), 'Failed to redirect to the main page via Logo'
