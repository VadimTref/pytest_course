from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def test_add_item_to_cart_from_catalog(driver, login_standard_user):
    add_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    add_button.click()

    cart_link = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    cart_link.click()

    cart_url = driver.current_url
    item_name = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link').text

    assert cart_url == 'https://www.saucedemo.com/cart.html'
    assert item_name == 'Sauce Labs Backpack'


def test_remove_item_from_cart_through_cart(driver, login_standard_user):
    wait = WebDriverWait(driver, 10)

    add_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    add_button.click()

    cart_link = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    cart_link.click()

    item = driver.find_element(By.CLASS_NAME, 'cart_item')

    qty_of_items_in_cart_badge = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    qty_of_items_in_cart_badge_before_remove = qty_of_items_in_cart_badge.text

    cart_badge_qty = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    cart_badge_qty_before_remove = wait.until(EC.visibility_of(cart_badge_qty))

    remove_button = driver.find_element(By.XPATH, '//button[@id="remove-sauce-labs-backpack"]')
    remove_button.click()

    qty_of_items_in_cart_badge_after_remove = qty_of_items_in_cart_badge.text
    cart_badge_qty_after_remove = wait.until(EC.invisibility_of_element(cart_badge_qty))

    try:
        driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    except NoSuchElementException:
        print("\n\nElement 'cart_badge_qty' does not exist")

    assert item.is_displayed() is False
    assert qty_of_items_in_cart_badge_before_remove == '1'
    assert qty_of_items_in_cart_badge_after_remove == ''
    assert cart_badge_qty_before_remove is not None
    assert cart_badge_qty_after_remove is True


def test_add_item_to_cart_from_product_card(driver, login_standard_user):
    item_name = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link>div')
    item_name.click()

    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4'
    # time.sleep(3)

    add_button = driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_button.click()
    # time.sleep(3)

    cart_link = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    cart_link.click()
    item_name = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link>div')
    # time.sleep(3)

    assert driver.current_url == 'https://www.saucedemo.com/cart.html'
    assert item_name.text == 'Sauce Labs Backpack'


def test_remove_item_from_cart_through_item_card(driver, login_standard_user):
    wait = WebDriverWait(driver, 10)

    item_name = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link>div')
    item_name.click()

    add_button = driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_button.click()

    cart_link = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    cart_link.click()

    item = driver.find_element(By.CLASS_NAME, 'cart_item')
    item_is_visible_before_remove = wait.until(EC.visibility_of(item))

    qty_of_items_in_cart_badge_before_remove = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').text

    cart_badge_qty = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    cart_badge_qty_before_remove = wait.until(EC.visibility_of(cart_badge_qty))

    driver.back()

    remove_button = driver.find_element(By.XPATH, '//button[@id="remove-sauce-labs-backpack"]')
    remove_button.click()

    cart_link = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    cart_link.click()

    qty_of_items_in_cart_badge_after_remove = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').text
    cart_badge_qty_after_remove = wait.until(EC.invisibility_of_element(cart_badge_qty))

    item_is_invisible_after_remove = wait.until(EC.invisibility_of_element(item))

    assert qty_of_items_in_cart_badge_before_remove == '1'
    assert qty_of_items_in_cart_badge_after_remove == ''
    assert cart_badge_qty_before_remove is not None
    assert cart_badge_qty_after_remove is True
    assert item_is_visible_before_remove is not None
    assert item_is_invisible_after_remove is True
