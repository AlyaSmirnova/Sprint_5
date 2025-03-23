from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import StellarBurgersLocators
from src.data import Data

class TestStellarBurgersRedirectionFromPersonalAccount:
    def test_redirection_from_personal_account_through_constructor_button(self, driver):
        driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_BUTTON))
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        constructor_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.CONSTRUCTOR_BUTTON))
        constructor_button.click()
        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.MAKE_AN_ORDER_BUTTON))
        assert driver.current_url == Config.URL, "Переход на страницу конструктора не произошел"

    def test_redirection_from_personal_account_trough_logo(self, driver):
        driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_BUTTON))
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGO)).click()
        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.MAKE_AN_ORDER_BUTTON))
        assert driver.current_url == Config.URL, "Переход на главную страницу не произошел"
