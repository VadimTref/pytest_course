import time

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
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    assert driver.current_url == 'https://the-internet.herokuapp.com/add_remove_elements/'


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 10)
    return wait


def test_add_elements(driver, open_source, wait):
    time.sleep(2)
    add_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add Element')]")
    add_button.click()
    add_button.click()
    add_button.click()

    delete_button_1 = driver.find_element(By.CSS_SELECTOR, '#elements > button:nth-child(1)')
    delete_buttons_list = driver.find_elements(By.CSS_SELECTOR, '#elements > button')

    assert delete_button_1.get_attribute('tagName') == 'BUTTON'
    assert delete_button_1.get_attribute('class') == 'added-manually'
    assert delete_button_1.get_attribute('onclick') == 'deleteElement()'
    assert delete_button_1.text == 'Delete'
    assert len(delete_buttons_list) == 3


def test_remove_elements(driver, open_source, wait):
    time.sleep(2)
    add_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add Element')]")
    add_button.click()
    add_button.click()
    add_button.click()

    delete_buttons_list = driver.find_elements(By.CSS_SELECTOR, '#elements > button')

    for element in driver.find_elements(By.CSS_SELECTOR, '#elements > button'):
        element.click()
        delete_buttons_list = driver.find_elements(By.CSS_SELECTOR, '#elements > button')

    assert len(delete_buttons_list) == 0

