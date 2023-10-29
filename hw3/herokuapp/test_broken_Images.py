import pytest
from selenium.webdriver.common.by import By
import requests


@pytest.fixture
def open_source(driver):
    driver.get('https://the-internet.herokuapp.com/broken_images')
    assert driver.current_url == 'https://the-internet.herokuapp.com/broken_images'


def test_broken_images(driver, open_source):
    images_list = driver.find_elements(By.TAG_NAME, 'img')
    broken_images_list = []
    for image in images_list:
        response = requests.get(image.get_attribute('src'))
        print(f"\n{response.status_code}")
        if response.status_code != 200:
            broken_images_list.append(image.get_attribute('src').split('/')[-1])
    print(broken_images_list)

    assert broken_images_list == ['asdf.jpg', 'hjkl.jpg']
