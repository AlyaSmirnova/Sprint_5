import pytest
from selenium import webdriver
from src.config import Config
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    chrome = webdriver.Chrome(options=options)
    chrome.get(Config.URL)
    yield chrome
    chrome.quit()
