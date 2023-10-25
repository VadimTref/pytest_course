import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


@pytest.fixture
def open_source(driver, wait):
    driver.get('https://victoretc.github.io/selenium_waits/')
    assert driver.current_url == 'https://victoretc.github.io/selenium_waits/'
    start_test_button = wait.until(EC.visibility_of_element_located((By.ID, 'startTest')))
    start_test_button.click()


@pytest.fixture
def login(driver):
    driver.find_element(By.ID, 'login').send_keys('qwerty')
    driver.find_element(By.ID, 'password').send_keys('qwerty')
    driver.find_element(By.ID, 'agree').click()
    driver.find_element(By.ID, 'register').click()


def test_registration_explicitly_wait(driver, open_source, login, wait):
    header_h1 = driver.find_element(By.TAG_NAME, 'h1').text
    assert header_h1 == 'Практика с ожиданиями в Selenium'

    loader = driver.find_element(By.ID, 'loader')
    assert loader.is_displayed()

    message = wait.until(EC.visibility_of_element_located((By.ID, 'successMessage'))).text
    assert message == 'Вы успешно зарегистрированы!'
