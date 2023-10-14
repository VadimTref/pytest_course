from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)


def test_add_item_to_cart_from_catalog():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    add_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    add_button.click()

    cart_link = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    cart_link.click()

    cart_url = driver.current_url
    item_name = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link').text

    assert cart_url == 'https://www.saucedemo.com/cart.html'
    assert item_name == 'Sauce Labs Backpack'

    driver.quit()


def test_remove_item_from_cart_through_cart():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(1)
    add_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    add_button.click()

    time.sleep(1)
    cart_link = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    cart_link.click()

    time.sleep(1)
    cart_badge_qty = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    item = driver.find_element(By.CLASS_NAME, 'cart_item')

    assert cart_badge_qty.text == '1'

    time.sleep(1)
    remove_button = driver.find_element(By.XPATH, '//button[@id="remove-sauce-labs-backpack"]')
    remove_button.click()

    time.sleep(1)
    cart_badge_qty = wait.until(EC.invisibility_of_element(cart_badge_qty))

    # try:
    #     driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    # except NoSuchElementException:
    #     print("Element does not exist")

    assert cart_badge_qty is True
    assert item.is_displayed() is False

    driver.quit()


def test_add_item_to_cart_from_product_card():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_name = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link>div')
    item_name.click()

    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4'
    time.sleep(3)

    add_button = driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_button.click()
    time.sleep(3)

    cart_link = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    cart_link.click()
    item_name = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link>div')
    time.sleep(3)

    assert driver.current_url == 'https://www.saucedemo.com/cart.html'
    assert item_name.text == 'Sauce Labs Backpack'

    driver.quit()


def test_remove_item_from_cart_through_item_card():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_name = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link>div')
    item_name.click()

    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4'
    time.sleep(3)

    add_button = driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_button.click()

    time.sleep(1)
    cart_link = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container')
    cart_link.click()

    cart_badge_qty = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')

    assert cart_badge_qty.text == '1'

    time.sleep(1)
    item = driver.find_element(By.CLASS_NAME, 'cart_item')

    assert item.is_displayed()

    driver.back()

    time.sleep(1)
    remove_button = driver.find_element(By.XPATH, '//button[@id="remove-sauce-labs-backpack"]')
    remove_button.click()

    time.sleep(3)

    cart_link = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container')
    cart_link.click()

    time.sleep(3)
    cart_badge_qty = wait.until(EC.invisibility_of_element(cart_badge_qty))
    item = wait.until(EC.invisibility_of_element(item))

    assert cart_badge_qty is True
    assert item is True

    driver.quit()
