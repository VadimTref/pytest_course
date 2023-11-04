import pytest
from hw2.pages.login_page import LoginPage
from hw2.data.data import MAIN_PAGE_URL, PRODUCTS_PAGE_URL, ITEMS_LOGIN_AND_PASSWORD, ITEMS_FAKE_LOGIN_AND_PASSWORD


class TestAuth:

    def test_auth_pos(self, driver):
        page = LoginPage(driver, MAIN_PAGE_URL)
        page.open_browser()
        page.login_standard_user()

        assert driver.current_url == PRODUCTS_PAGE_URL

    def test_auth_neg(self, driver):
        page = LoginPage(driver, MAIN_PAGE_URL)
        page.open_browser()
        error_message = page.login_fake_user()

        assert error_message == 'Epic sadface: Username and password do not match any user in this service'

    @pytest.mark.parametrize("items", ITEMS_LOGIN_AND_PASSWORD)
    def test_auth_positive(self, driver, items):
        login, password = items
        page = LoginPage(driver, MAIN_PAGE_URL)
        page.open_browser()
        page.login_parametrize_user(login, password)

        assert driver.current_url == PRODUCTS_PAGE_URL

    # @pytest.mark.failed_auth
    @pytest.mark.parametrize("items", ITEMS_FAKE_LOGIN_AND_PASSWORD)
    def test_auth_negative(self, driver, items):
        login, password = items
        page = LoginPage(driver, MAIN_PAGE_URL)
        page.open_browser()
        error_message = page.login_parametrize_fake_user(login, password)

        assert error_message == 'Epic sadface: Username and password do not match any user in this service'
