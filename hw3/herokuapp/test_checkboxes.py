import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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
    driver.get('https://the-internet.herokuapp.com/checkboxes')
    assert driver.current_url == 'https://the-internet.herokuapp.com/checkboxes'


def test_checkboxes_select_deselect(driver, open_source):
    checkbox_1 = driver.find_element(By.CSS_SELECTOR, '#checkboxes input:nth-child(1)')
    checkbox_1.click()
    checkboxes_list = driver.find_elements(By.CSS_SELECTOR, '[type="checkbox"]')

    for checkbox in checkboxes_list:
        assert checkbox.get_attribute('checked')
        assert checkbox.is_selected()

    for checkbox in checkboxes_list:
        checkbox.click()
        assert checkbox.get_attribute('checked') is None
        assert checkbox.is_selected() is False

# def test_checkboxes_unselect(driver, open_source):
#     checkbox_2 = driver.find_element(By.CSS_SELECTOR, '#checkboxes input:nth-of-type(2)')
#     time.sleep(2)
#     checkbox_2.click()
#     time.sleep(2)
#     checkboxes_list = driver.find_elements(By.CSS_SELECTOR, '[type="checkbox"]')
#
#     for checkbox in checkboxes_list:
#         time.sleep(2)
#         assert checkbox.get_attribute('checked') is None
#         assert checkbox.is_selected() is False
