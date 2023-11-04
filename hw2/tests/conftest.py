import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from hw2.data.data import MAIN_PAGE_URL
from hw2.pages.login_page import LoginPage


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--incognito')
    # options.add_argument('--window-size=2880,1800')
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 10)
    return wait


@pytest.fixture(scope='function')
def login_standard_user(driver):
    page = LoginPage(driver, MAIN_PAGE_URL)
    page.open_browser()
    page.login_standard_user()

#     driver.get(MAIN_PAGE_URL)
#     driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)
#     driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
#     driver.find_element(By.XPATH, LOGIN_BUTTON).click()
#     yield
