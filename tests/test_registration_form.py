from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.helpers import generate_registration_user
from src.locators import StellarBurgersLocators

class TestStellarBurgersRegistration:
    def test_successful_registration(self, driver):
        driver.get(f'{Config.URL}/register'.rstrip('/'))
        test_user = generate_registration_user()
        driver.find_element(*StellarBurgersLocators.NAME_FIELD).send_keys(test_user['name'])
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(test_user['email'])
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(test_user['password'])
        driver.find_element(*StellarBurgersLocators.SUBMIT_BUTTON).click()
        login_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_BUTTON))

        assert login_button.is_displayed(), 'Кнопка "Войти" не отображается, регистрация не пройдена'

    def test_registration_with_short_password(self, driver):
        driver.get(f'{Config.URL}/register'.rstrip('/'))
        test_user = generate_registration_user()
        test_user['password'] = '1593'
        driver.find_element(*StellarBurgersLocators.NAME_FIELD).send_keys(test_user['name'])
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(test_user['email'])
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(test_user['password'])
        driver.find_element(*StellarBurgersLocators.SUBMIT_BUTTON).click()

        password_error_message = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.PASSWORD_ERROR_MESSAGE))

        assert 'Некорректный пароль' in password_error_message.text, 'Пароль должен быть не меньше 6 символов'
