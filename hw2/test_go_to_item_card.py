import pytest
from selenium.webdriver.common.by import By

expected_items_url = ['https://www.saucedemo.com/inventory-item.html?id=4',
                      'https://www.saucedemo.com/inventory-item.html?id=0',
                      'https://www.saucedemo.com/inventory-item.html?id=1',
                      'https://www.saucedemo.com/inventory-item.html?id=5',
                      'https://www.saucedemo.com/inventory-item.html?id=2',
                      'https://www.saucedemo.com/inventory-item.html?id=3'
                      ]

expected_items_names = ['Sauce Labs Backpack',
                        'Sauce Labs Bike Light',
                        'Sauce Labs Bolt T-Shirt',
                        'Sauce Labs Fleece Jacket',
                        'Sauce Labs Onesie',
                        'Test.allTheThings() T-Shirt (Red)'
                        ]


def test_go_to_item_card_after_click_on_img(driver, login_standard_user):
    items_img = driver.find_elements(By.CSS_SELECTOR, '[id$="_img_link"]')
    actual_items_url = []
    actual_items_names = []

    for img in range(len(items_img)):
        items_img[img].click()
        actual_items_url.append(driver.current_url)
        actual_items_names.append(driver.find_element(By.CSS_SELECTOR, '.inventory_details_name').text)
        button_back = driver.find_element(By.ID, 'back-to-products')
        button_back.click()
        items_img = driver.find_elements(By.CSS_SELECTOR, '[id$= "_img_link"]')

    assert actual_items_url == expected_items_url
    assert actual_items_names == expected_items_names


def test_go_to_item_card_after_click_on_name(driver, login_standard_user):

    items_name = driver.find_elements(By.CSS_SELECTOR, '[id$="_title_link"]')
    actual_items_url = []
    actual_items_names = []

    for name in range(len(items_name)):
        items_name[name].click()
        actual_items_url.append(driver.current_url)
        actual_items_names.append(driver.find_element(By.CSS_SELECTOR, '.inventory_details_name').text)
        button_back = driver.find_element(By.ID, 'back-to-products')
        button_back.click()
        items_name = driver.find_elements(By.CSS_SELECTOR, '[id$= "_title_link"]')

    assert actual_items_url == expected_items_url
    assert actual_items_names == expected_items_names


@pytest.mark.parametrize("selector", ['item_4_img_link',
                                      'item_2_img_link',
                                      'item_1_img_link'])
def test_click_on_img(driver, login_standard_user, selector):
    img_selector = selector
    driver.find_element(By.ID, img_selector).click()
    assert driver.current_url != "https://www.saucedemo.com/inventory.html"


@pytest.mark.parametrize("selector", ['item_0_title_link',
                                      'item_1_title_link',
                                      'item_2_title_link'])
def test_click_on_title(driver, login_standard_user, selector):
    title_selector = selector
    driver.find_element(By.ID, title_selector).click()
    assert driver.current_url != "https://www.saucedemo.com/inventory.html"
