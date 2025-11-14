from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import StellarBurgersLocators

class TestStellarBurgersTransitionToSections:
    def test_transition_to_section_buns(self, driver):
        element = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUNS_SECTION))
        driver.execute_script("arguments[0].click()", element)
        active_buns_section = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.ACTIVE_BUNS_SECTION))
        assert "current" in active_buns_section.get_attribute("class"), "Переход в раздел 'Булки' не произошел"

    def test_transition_to_section_sauces(self, driver):
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.SAUCES_SECTION)).click()
        active_sauces_section = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.ACTIVE_SAUCES_SECTION))
        assert "current" in active_sauces_section.get_attribute("class"), "Переход в раздел 'Соусы' не произошел"

    def test_transition_to_section_addings(self, driver):
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.ADDINGS_SECTION)).click()
        active_addings_section = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.ACTIVE_ADDINGS_SECTION))
        assert "current" in active_addings_section.get_attribute("class"), "Переход в раздел 'Начинки' не произошел"
