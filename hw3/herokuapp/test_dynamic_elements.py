import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def open_source(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading')
    assert driver.current_url == 'https://the-internet.herokuapp.com/dynamic_loading'


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
