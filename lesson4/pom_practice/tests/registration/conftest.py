from faker import Faker 
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def random_email():
    faker = Faker()
    return faker.email()

