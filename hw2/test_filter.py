from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_filter_a_to_z(driver, login_standard_user):

    item_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')

    item_name_list = []
    for item in item_list:
        item_name_list.append(item.text)

    sorted_item_name_list = sorted(item_name_list)
    print(f'\n{sorted_item_name_list}')

    select = Select(driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    select.select_by_value('az')

    filtered_item_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')

    filtered_item_name_list = []
    for item in filtered_item_list:
        filtered_item_name_list.append(item.text)
    print(filtered_item_name_list)

    assert sorted_item_name_list == filtered_item_name_list


def test_filter_z_to_a(driver, login_standard_user):

    item_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')

    item_name_list = [item.text for item in item_list]

    sorted_item_name_list = sorted(item_name_list, reverse=True)
    print(f'\n{sorted_item_name_list}')

    select = Select(driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    select.select_by_value('za')

    filtered_item_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')

    filtered_item_name_list = [item.text for item in filtered_item_list]
    print(filtered_item_name_list)

    assert sorted_item_name_list == filtered_item_name_list


def test_filter_low_to_high(driver, login_standard_user):

    item_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')

    item_price_list = [float(item.text.replace('$', '')) for item in item_list]
    sorted_item_price_list = sorted(item_price_list)
    print(f'\n{sorted_item_price_list}')

    select = Select(driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    select.select_by_value('lohi')

    filtered_item_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')

    filtered_item_price_list = [float(item.text.replace('$', '')) for item in filtered_item_list]
    print(filtered_item_price_list)

    assert sorted_item_price_list == filtered_item_price_list


def test_filter_high_to_low(driver, login_standard_user):

    item_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')

    item_price_list = [float(item.text.replace('$', '')) for item in item_list]
    sorted_item_price_list = sorted(item_price_list, reverse=True)
    print(f'\n{sorted_item_price_list}')

    select = Select(driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    select.select_by_value('hilo')

    filtered_item_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')

    filtered_item_price_list = [float(item.text.replace('$', '')) for item in filtered_item_list]
    print(filtered_item_price_list)

    assert sorted_item_price_list == filtered_item_price_list
