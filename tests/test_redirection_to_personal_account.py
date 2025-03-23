from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import StellarBurgersLocators
from src.data import Data

class TestStellarBurgersRedirectionToPersonalAccount:
    def test_redirection_to_personal_account(self, driver):
        driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_BUTTON))
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        assert "/account/profile" in driver.current_url, "Переход на страницу личного кабинета не произошел"
