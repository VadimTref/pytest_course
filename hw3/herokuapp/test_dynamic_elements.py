import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def chrome_options():
    options = Options()
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    return options


@pytest.fixture()
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    # driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def open_source(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading')
    assert driver.current_url == 'https://the-internet.herokuapp.com/dynamic_loading'


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


def test_element_is_hidden(driver, open_source, wait):
    example_1 = driver.find_element(By.CSS_SELECTOR, '[href$="1"]')
    example_1.click()

    start_button = driver.find_element(By.CSS_SELECTOR, '#start > button')
    start_button.click()

    text = driver.find_element(By.ID, 'finish')

    assert wait.until(EC.presence_of_element_located((By.ID, 'finish')))
    assert text.is_displayed() is False

    assert wait.until(EC.visibility_of_element_located((By.ID, 'finish')))
    assert text.is_displayed()


def test_element_rendered_after_fact(driver, open_source, wait):
    example_2 = driver.find_element(By.CSS_SELECTOR, '[href$="2"]')
    example_2.click()

    start_button = driver.find_element(By.CSS_SELECTOR, '#start > button')
    start_button.click()

    text = wait.until(EC.invisibility_of_element_located((By.ID, 'finish')))
    assert text is True

    text = wait.until(EC.visibility_of_element_located((By.ID, 'finish')))
    assert text
    assert text.is_displayed
