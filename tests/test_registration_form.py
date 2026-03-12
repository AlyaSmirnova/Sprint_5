import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.helpers import generate_registration_user
from src.locators import StellarBurgersLocators


@allure.suite('User Authentication Tests')
@allure.feature('User Registration')
class TestStellarBurgersRegistration:

    @allure.title('Successful user registration')
    @allure.description('Verify that a user can register with valid name, email, and password (min 6 characters)')
    def test_successful_registration(self, driver):
        with allure.step('Navigate to registration page'):
            driver.get(f'{Config.URL}/register'.rstrip('/'))
        with allure.step('Generate test user data'):
            test_user = generate_registration_user()
        with allure.step('Fill registration form and submit'):
            driver.find_element(*StellarBurgersLocators.NAME_FIELD).send_keys(test_user['name'])
            driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(test_user['email'])
            driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(test_user['password'])
            driver.find_element(*StellarBurgersLocators.SUBMIT_BUTTON).click()
        with allure.step('Verify redirection to Login page'):
            login_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_BUTTON))
            assert login_button.is_displayed(), 'Registration failed: Login button not visible after signup'

    @allure.title('Registration failure due to short password')
    @allure.description('Verify that registration fails and an error message appears when the password is less than 6 characters')
    def test_registration_with_short_password(self, driver):
        with allure.step('Navigate to registration page'):
            driver.get(f'{Config.URL}/register'.rstrip('/'))
        with allure.step('Generate user with short password (4 characters)'):
            test_user = generate_registration_user()
            test_user['password'] = '1593'
        with allure.step('Fill form and submit'):
            driver.find_element(*StellarBurgersLocators.NAME_FIELD).send_keys(test_user['name'])
            driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(test_user['email'])
            driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(test_user['password'])
            driver.find_element(*StellarBurgersLocators.SUBMIT_BUTTON).click()
        with allure.step('Verify error message "Incorrect password"'):
            password_error_message = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.PASSWORD_ERROR_MESSAGE))
            assert 'Некорректный пароль' in password_error_message.text, 'Error message for short password did not appear'
