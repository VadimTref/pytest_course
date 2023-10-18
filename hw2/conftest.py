import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from hw2.update.data import MAIN_PAGE_URL, LOGIN, PASSWORD
from hw2.update.locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def login_standard_user(driver):
    driver.get(MAIN_PAGE_URL)
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    yield
