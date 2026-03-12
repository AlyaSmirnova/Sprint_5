import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import StellarBurgersLocators
from src.data import Data


@allure.suite('Navigation Tests')
@allure.feature('Personal Account Access')
class TestStellarBurgersRedirectionToPersonalAccount:

    @allure.title('Access Personal Account from Main Page')
    @allure.description('Verify that an authorized user can navigate to the Personal Account section via the header button')
    def test_redirection_to_personal_account(self, driver):
        with allure.step('Authorize with valid credentials'):
            driver.find_element(*StellarBurgersLocators.ACCOUNT_LOGIN_BUTTON).click()
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_BUTTON))
            driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(Data.LOGIN)
            driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)
            driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        with allure.step('Wait for overlay to disappear and click "Personal Account"'):
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.invisibility_of_element_located(StellarBurgersLocators.MODAL_OVERLAY))
        with allure.step('Click on "Personal Account" button'):
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        with allure.step('Verify redirection to Account page'):
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains("/account"))
            assert "/account" in driver.current_url, 'Failed to redirect to the Personal Account page'
