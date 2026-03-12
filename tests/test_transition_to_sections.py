import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import StellarBurgersLocators


@allure.suite('Constructor Tests')
@allure.feature('Ingredient Sections Navigation')
class TestStellarBurgersTransitionToSections:

    @allure.title('Switch to "Buns" section')
    @allure.description('Verify that the "Buns" tab becomes active when clicked')
    def test_transition_to_section_buns(self, driver):
        with allure.step('Click on "Buns" section tab'):
            element = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUNS_SECTION))
            driver.execute_script("arguments[0].click()", element)
        with allure.step('Verify "Buns" section is active'):
            active_buns_section = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.ACTIVE_BUNS_SECTION))
            assert "current" in active_buns_section.get_attribute("class"), 'Failed to switch to "Buns" section'

    @allure.title('Switch to "Sauces" section')
    def test_transition_to_section_sauces(self, driver):
        with allure.step('Click on "Sauces" section tab'):
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.SAUCES_SECTION)).click()
        with allure.step('Verify "Sauces" section is active'):
            active_sauces_section = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.ACTIVE_SAUCES_SECTION))
            assert "current" in active_sauces_section.get_attribute("class"), 'Failed to switch to "Sauces" section'

    @allure.title('Switch to "Fillings" section')
    def test_transition_to_section_addings(self, driver):
        with allure.step('Click on "Fillings" section tab'):
            WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.ADDINGS_SECTION)).click()
        with allure.step('Verify "Fillings" section is active'):
            active_addings_section = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.ACTIVE_ADDINGS_SECTION))
            assert "current" in active_addings_section.get_attribute("class"), 'Failed to switch to "Fillings" section'
