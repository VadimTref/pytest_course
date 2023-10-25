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
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def open_source(driver):
    driver.get('https://victoretc.github.io/selenium_waits/')

    start_test_button = driver.find_element(By.ID, 'startTest')
    start_test_button.click()


@pytest.fixture
def login(driver):
    driver.find_element(By.ID, 'login').send_keys('qwerty')
    driver.find_element(By.ID, 'password').send_keys('qwerty')
    driver.find_element(By.ID, 'agree').click()
    driver.find_element(By.ID, 'register').click()


def test_registration_implicitly_wait(driver, open_source, login):
    header_h1 = driver.find_element(By.TAG_NAME, 'h1').text
    assert header_h1 == 'Практика с ожиданиями в Selenium'

    loader = driver.find_element(By.ID, 'loader')
    assert loader.is_displayed()

    message = driver.find_element(By.ID, 'successMessage')
    assert message.text == 'Вы успешно зарегистрированы!'


