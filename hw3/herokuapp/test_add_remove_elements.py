import pytest

from hw3.herokuapp.data.data import ADD_REMOVE_ELEMENTS_URL
from hw3.herokuapp.locators.locators import ADD_BUTTON, DELETE_BUTTON, DELETE_BUTTON_LIST


@pytest.fixture
def open_source(driver):
    driver.get(ADD_REMOVE_ELEMENTS_URL)
    assert driver.current_url == ADD_REMOVE_ELEMENTS_URL


def test_add_elements(driver, open_source, wait):
    add_button = driver.find_element(*ADD_BUTTON)
    add_button.click()
    add_button.click()
    add_button.click()

    delete_button_1 = driver.find_element(*DELETE_BUTTON)
    delete_buttons_list = driver.find_elements(*DELETE_BUTTON_LIST)

    assert delete_button_1.get_attribute('tagName') == 'BUTTON'
    assert delete_button_1.get_attribute('class') == 'added-manually'
    assert delete_button_1.get_attribute('onclick') == 'deleteElement()'
    assert delete_button_1.text == 'Delete'
    assert len(delete_buttons_list) == 3


# def test_remove_elements(driver, open_source, wait):
#     add_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add Element')]")
#     add_button.click()
#     add_button.click()
#     add_button.click()
#
#     delete_buttons_list = driver.find_elements(By.CSS_SELECTOR, '#elements > button')
#
#     for element in driver.find_elements(By.CSS_SELECTOR, '#elements > button'):
#         element.click()
#         delete_buttons_list = driver.find_elements(By.CSS_SELECTOR, '#elements > button')
#
#     assert len(delete_buttons_list) == 0
