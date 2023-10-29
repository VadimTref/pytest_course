import pytest
from selenium.webdriver.common.by import By


@pytest.fixture
def open_source(driver):
    driver.get('https://the-internet.herokuapp.com/basic_auth')
    assert driver.current_url == 'https://the-internet.herokuapp.com/basic_auth'


def test_basic_auth(driver, open_source, wait):
    driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

    assert (driver.find_element(By.CSS_SELECTOR, '.example p').text ==
            'Congratulations! You must have the proper credentials.')

