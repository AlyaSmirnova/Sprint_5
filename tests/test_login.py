import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import StellarBurgersLocators
from src.data import Data


@allure.suite('User Authentication Tests')
@allure.feature('Login Functionality')
class TestStellarBurgersLogin:

    @allure.title('Verify Main Page URL')
    @allure.description('Check if the application opens the correct URL')
    def test_main_page(self, driver):
        with allure.step('Compare current URL with expected URL'):
            assert driver.current_url.rstrip('/') == f'{Config.URL}'.rstrip('/'), "Url is wrong"

    @allure.title('Login via "Login to Account" button on Main Page')
    def test_login_from_main_page(self, driver):
        with allure.step('Click "Login to Account" button'):
            driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN_BUTTON).click()
        with allure.step('Wait for Login page to load'):
            login_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_BUTTON))
            assert login_button.is_displayed(), 'Login button not visible'
        with allure.step('Enter credentials and submit'):
            driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(Data.LOGIN)
            driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
            driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        with allure.step('Verify successful login'):
            make_an_order_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.MAKE_AN_ORDER_BUTTON))
            assert make_an_order_button.is_displayed(), 'Login failed: "Make Order" button not found'

    @allure.title('Login via "Personal Account" button in header')
    def test_login_from_button_personal_account(self, driver):
        with allure.step('Click "Personal Account" button'):
            driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        with allure.step('Enter credentials and login'):
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_HEADER))
            driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(Data.LOGIN)
            driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
            driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        with allure.step('Verify successful login'):
            make_an_order_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.MAKE_AN_ORDER_BUTTON))
            assert make_an_order_button.is_displayed(), 'User is not logged in'

    @allure.title('Login via link on Registration page')
    def test_login_from_login_button_in_registration_page(self, driver):
        with allure.step('Navigate to Registration page'):
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.ACCOUNT_LOGIN_BUTTON)).click()
            registration_link = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.REGISTRATION_LINK))
            driver.execute_script("arguments[0].scrollIntoView();", registration_link)
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.REGISTRATION_LINK)).click()
            assert "/register" in driver.current_url, 'Failed to navigate to registration page'

        with allure.step('Click "Login" link and enter credentials'):
            login_link = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.LOGIN_LINK))
            driver.execute_script("arguments[0].scrollIntoView();", login_link)
            login_link.click()

            driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(Data.LOGIN)
            driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
            driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        with allure.step('Verify successful login'):
            make_an_order_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.MAKE_AN_ORDER_BUTTON))
            assert make_an_order_button.is_displayed(), 'Login failed via registration page'

    @allure.title('Login via "Login" link on Password Recovery page')
    def test_login_through_password_recovery_link(self, driver):
        with allure.step('Navigate to Password Recovery page'):
            driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN_BUTTON).click()
            recovery_password_link = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.RECOVERY_PASSWORD_LINK))
            driver.execute_script("arguments[0].scrollIntoView();", recovery_password_link)
            recovery_password_link.click()
        with allure.step('Click "Login" and authorize'):
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGIN_LINK_ON_RECOVERY_PASSWORD_PAGE)).click()
            driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(Data.LOGIN)
            driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
            driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        with allure.step('Verify successful login'):
            make_an_order_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.MAKE_AN_ORDER_BUTTON))
            assert make_an_order_button.is_displayed(), 'Login failed via password recovery page'
