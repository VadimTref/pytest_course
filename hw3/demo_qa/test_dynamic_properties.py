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


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


def hex_to_rgba(hex_color, alpha):
    hex_color = hex_color.lstrip('#')

    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    alpha = max(0.0, min(1, alpha))

    rgba = f"rgba({red}, {green}, {blue}, {alpha})"
    return rgba


def test_button_enable_after(driver, wait):
    driver.get('https://demoqa.com/dynamic-properties')
    assert driver.current_url == 'https://demoqa.com/dynamic-properties'

    button_enable_after = driver.find_element(By.ID, 'enableAfter')

    assert button_enable_after.is_displayed()
    assert button_enable_after.is_enabled() is False

    button_enable_after = wait.until(EC.element_to_be_clickable((By.ID, 'enableAfter')))
    assert button_enable_after.is_enabled()


def test_button_color_change(driver, wait):
    driver.get('https://demoqa.com/dynamic-properties')
    assert driver.current_url == 'https://demoqa.com/dynamic-properties'

    button_color_change = driver.find_element(By.ID, 'colorChange')
    assert button_color_change.is_displayed()
    assert button_color_change.is_enabled()
    assert button_color_change.value_of_css_property('color') == hex_to_rgba('#ffffff', 1)
    # print(button_color_change.value_of_css_property('color'))

    button_color_change = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'text-danger')))
    assert button_color_change.value_of_css_property('color') == hex_to_rgba('#dc3545', 1)


def test_button_visible_after(driver, wait):
    driver.get('https://demoqa.com/dynamic-properties')
    assert driver.current_url == 'https://demoqa.com/dynamic-properties'

    button_visible_after = wait.until(EC.invisibility_of_element_located((By.ID, 'visibleAfter')))
    assert button_visible_after is True

    button_visible_after = wait.until(EC.visibility_of_element_located((By.ID, 'visibleAfter')))
    assert button_visible_after.is_displayed()
    assert button_visible_after.is_enabled()
