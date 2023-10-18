from selenium.webdriver.common.by import By


def test_order_item(driver, login_standard_user):

    add_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    add_button.click()

    cart_link = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    cart_link.click()

    checkout_button = driver.find_element(By.ID, 'checkout')
    checkout_button.click()

    driver.find_element(By.ID, 'first-name').send_keys('Yu')
    driver.find_element(By.ID, 'last-name').send_keys('Wong')
    driver.find_element(By.ID, 'postal-code').send_keys('12345')
    driver.find_element(By.ID, 'continue').click()

    item_name = driver.find_element(By.CSS_SELECTOR, '.inventory_item_name').text
    item_qty = driver.find_element(By.CSS_SELECTOR, '.cart_quantity').text
    item_price = driver.find_element(By.CSS_SELECTOR, '.inventory_item_price').text

    item_tax = driver.find_element(By.CSS_SELECTOR, '.summary_tax_label').text
    expected_item_tax = f'Tax: ${str(round((float(item_price.replace("$", "")) * 0.08), 2))}0'

    item_price_total = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
    expected_item_price_total = \
        f'Total: ${float(item_price.replace("$", "")) + float(expected_item_tax.replace("Tax: $", ""))}'

    driver.find_element(By.ID, 'finish').click()

    complete_message = driver.find_element(By.TAG_NAME, 'h2').text

    assert driver.current_url == 'https://www.saucedemo.com/checkout-complete.html'
    assert item_name == 'Sauce Labs Backpack'
    assert item_qty == '1'
    assert item_price == '$29.99'
    assert item_tax == expected_item_tax
    assert item_price_total == expected_item_price_total
    assert complete_message == 'Thank you for your order!'

