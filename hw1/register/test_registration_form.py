import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)


@pytest.fixture
def hex_to_rgba(hex_color, alpha):
    hex_color = hex_color.lstrip('#')

    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    alpha = max(0.0, min(1, alpha))

    rgba = f"rgba({red}, {green}, {blue}, {alpha})"

    yield rgba


@pytest.mark.parametrize('hex_color, alpha', [('#dddddd', 1)])
def test_elements_before_filling(hex_to_rgba):
    driver.get('https://victoretc.github.io/webelements_information/')

    name_field = driver.find_element(By.ID, 'username')
    password_field = driver.find_element(By.ID, 'password')

    checkbox = driver.find_element(By.CSS_SELECTOR, '#agreement')
    reg_button = driver.find_element(By.ID, 'registerButton')
    print(f"\n{checkbox.get_attribute('disabled')}")
    print(reg_button.get_attribute('disabled'))

    assert name_field.is_enabled()
    assert password_field.is_enabled()

    assert checkbox.get_attribute('disabled') is None
    assert checkbox.is_selected() is False

    assert reg_button.get_attribute('disabled')
    assert reg_button.is_enabled() is False
    assert reg_button.value_of_css_property('background-color') == hex_to_rgba

    driver.quit()


@pytest.mark.parametrize('hex_color, alpha', [('#007BFF', 1)])
def test_elements_after_filling(hex_to_rgba):
    driver.get('https://victoretc.github.io/webelements_information/')

    driver.find_element(By.ID, 'username').send_keys('Vadim')
    driver.find_element(By.ID, 'password').send_keys('Test Password')

    checkbox = driver.find_element(By.ID, 'agreement')
    reg_button = driver.find_element(By.ID, 'registerButton')

    time.sleep(1)
    checkbox.click()
    time.sleep(1)

    print(f"\n{checkbox.get_attribute('disabled')}")
    print(reg_button.get_attribute('disabled'))

    assert checkbox.get_attribute('disabled') is None
    assert checkbox.is_selected()

    assert reg_button.get_attribute('disabled') is None
    assert reg_button.is_enabled()
    assert reg_button.value_of_css_property('background-color') == hex_to_rgba

    driver.quit()
