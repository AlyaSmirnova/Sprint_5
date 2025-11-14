from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import StellarBurgersLocators
from src.data import Data

class TestStellarBurgersLogin:
    def test_main_page(self, driver):
        assert driver.current_url.rstrip('/') == f'{Config.URL}'.rstrip('/'), "Url is wrong"

    def test_login_from_main_page(self, driver):
        driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN_BUTTON).click()
        login_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_BUTTON))
        assert login_button.is_displayed(), 'Кнопка "Войти" не отображается, невозможно зайти в Личный кабинет'
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()

        make_an_order_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.MAKE_AN_ORDER_BUTTON))
        assert make_an_order_button.is_displayed(), 'Кнопка "Оформить заказ" не отображается, Вы не вошли в личный кабинет'

    def test_login_from_button_personal_account(self, driver):
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_HEADER))
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        make_an_order_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.MAKE_AN_ORDER_BUTTON))
        assert make_an_order_button.is_displayed(), 'Кнопка "Оформить заказ" не отображается, Вы не вошли в личный кабинет'

    def test_login_from_login_button_in_registration_page(self, driver):
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.ACCOUNT_LOGIN_BUTTON)).click()
        registration_link = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.REGISTRATION_LINK))
        driver.execute_script("arguments[0].scrollIntoView();", registration_link)
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.REGISTRATION_LINK)).click()
        assert "/register" in driver.current_url, "Страница регистрации не загрузилась"

        login_link = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.LOGIN_LINK))
        driver.execute_script("arguments[0].scrollIntoView();", login_link)
        login_link.click()

        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        make_an_order_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.MAKE_AN_ORDER_BUTTON))
        assert make_an_order_button.is_displayed(), 'Кнопка "Оформить заказ" не отображается, Вы не вошли в личный кабинет'

    def test_login_through_password_recovery_link(self, driver):
        driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN_BUTTON).click()
        recovery_password_link = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.RECOVERY_PASSWORD_LINK))
        driver.execute_script("arguments[0].scrollIntoView();", recovery_password_link)
        recovery_password_link.click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGIN_LINK_ON_RECOVERY_PASSWORD_PAGE)).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        make_an_order_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.MAKE_AN_ORDER_BUTTON))
        assert make_an_order_button.is_displayed(), 'Кнопка "Оформить заказ" не отображается, Вы не вошли в личный кабинет'
