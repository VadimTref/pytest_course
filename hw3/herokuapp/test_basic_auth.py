import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--incognito')
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def open_source(driver):
    driver.get('https://the-internet.herokuapp.com/basic_auth')
    assert driver.current_url == 'https://the-internet.herokuapp.com/basic_auth'


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 10)
    return wait


def test_basic_auth(driver, open_source, wait):
    driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

    assert (driver.find_element(By.CSS_SELECTOR, '.example p').text ==
            'Congratulations! You must have the proper credentials.')

