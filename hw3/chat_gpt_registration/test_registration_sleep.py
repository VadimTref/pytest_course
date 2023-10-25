import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def chrome_options():
    options = Options()
    # options.add_argument('--window-size=100,100')
    # options.add_argument('--incognito')
    # options.add_argument('--headless')
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(By.ID, 'login').send_keys('qwerty')
    driver.find_element(By.ID, 'password').send_keys('qwerty')
    driver.find_element(By.ID, 'agree').click()
    driver.find_element(By.ID, 'register').click()
    yield


def test_registration_sleep(driver):
    driver.get('https://victoretc.github.io/selenium_waits/')
    header_h1 = driver.find_element(By.TAG_NAME, 'h1').text
    assert driver.current_url == 'https://victoretc.github.io/selenium_waits/'
    assert header_h1 == 'Практика с ожиданиями в Selenium'

    time.sleep(5)
    start_test_button = driver.find_element(By.ID, 'startTest')
    start_test_button.click()

    driver.find_element(By.ID, 'login').send_keys('qwerty')
    driver.find_element(By.ID, 'password').send_keys('qwerty')
    driver.find_element(By.ID, 'agree').click()
    driver.find_element(By.ID, 'register').click()

    loader = driver.find_element(By.ID, 'loader')
    assert loader.is_displayed()

    time.sleep(5)
    message = driver.find_element(By.ID, 'successMessage').text
    assert message == 'Вы успешно зарегистрированы!'
