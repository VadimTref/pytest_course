from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_logout():
    driver.get("https://www.saucedemo.com/")

    url_before = driver.current_url
    print(f'\n{url_before}')

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.CSS_SELECTOR, '#react-burger-menu-btn')
    burger_menu.click()

    time.sleep(1)
    logout = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
    logout.click()

    url_after = driver.current_url
    print(url_after)

    assert url_before == url_after

    driver.quit()


def test_about_button():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.CSS_SELECTOR, '#react-burger-menu-btn')
    burger_menu.click()

    time.sleep(1)
    about_button = driver.find_element(By.CSS_SELECTOR, '#about_sidebar_link')
    about_button.click()

    logo_sauce_labs = driver.find_element(By.XPATH, '//img[@src="/images/logo.svg"]')

    text = driver.find_element(By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-body1.css-sere2z').text

    assert driver.current_url == 'https://saucelabs.com/'
    assert logo_sauce_labs.is_displayed() is True
    assert text == ('The world relies on your code. Test on thousands of different device, '
                    'browser, and OS configurations–anywhere, any time.')

    driver.quit()


def test_reset_app_state_button():
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

    items_before_reset = len(driver.find_elements(By.CSS_SELECTOR, '.cart_item'))
    cart_badge_qty_before_reset = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').text

    burger_menu = driver.find_element(By.CSS_SELECTOR, '#react-burger-menu-btn')
    burger_menu.click()

    time.sleep(1)
    reset_app_state = driver.find_element(By.CSS_SELECTOR, '#reset_sidebar_link')
    reset_app_state.click()

    close_burger_menu = driver.find_element(By.CSS_SELECTOR, '#react-burger-cross-btn')
    close_burger_menu.click()

    driver.refresh()

    items_after_reset = len(driver.find_elements(By.CSS_SELECTOR, '.cart_item'))
    cart_badge_qty_after_reset = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').text

    assert items_before_reset == 1
    assert items_after_reset == 0
    assert cart_badge_qty_before_reset == '1'
    assert cart_badge_qty_after_reset == ''

    driver.quit()
