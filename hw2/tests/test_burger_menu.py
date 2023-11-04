from hw2.data.data import MAIN_PAGE_URL, SAUCE_LABS_PAGE_URL, PRODUCTS_PAGE_URL, CART_PAGE_URL
from hw2.pages.burger_menu_page import BurgerMenuPage
from hw2.pages.sauce_labs_page import SauceLabsPage
from hw2.pages.products_page import ProductsPage
from hw2.pages.cart_page import CartPage


class TestBurgerMenu:

    def test_logout_button(self, driver, login_standard_user):
        page = BurgerMenuPage(driver, MAIN_PAGE_URL)
        page.open_burger_menu()
        page.logout_button().click()

        assert driver.current_url == MAIN_PAGE_URL

    def test_about_button(self, driver, login_standard_user):
        page = BurgerMenuPage(driver, MAIN_PAGE_URL)
        page.open_burger_menu()
        page.about_button().click()

        page = SauceLabsPage(driver, SAUCE_LABS_PAGE_URL)
        logo = page.sauce_labs_logo()
        text = page.sauce_labs_text()

        assert driver.current_url == SAUCE_LABS_PAGE_URL
        assert logo.is_displayed()
        assert text == ('The world relies on your code. Test on thousands of different device, '
                        'browser, and OS configurations–anywhere, any time.')

    def test_reset_app_state_button(self, driver, login_standard_user):
        page = ProductsPage(driver, PRODUCTS_PAGE_URL)
        page.add_to_cart_button().click()
        page.cart_link().click()

        assert driver.current_url == CART_PAGE_URL

        page = CartPage(driver, CART_PAGE_URL)
        items_before_reset = page.cart_items_list()
        cart_badge_qty_before_reset = page.cart_link().text

        page = BurgerMenuPage(driver, MAIN_PAGE_URL)
        page.open_burger_menu()
        page.reset_app_state_button().click()
        page.close_burger_menu()

        page = CartPage(driver, CART_PAGE_URL)
        items_after_reset = page.cart_items_list_is_empty()
        cart_badge_qty_after_reset = page.cart_link().text

        assert len(items_before_reset) == 1
        assert items_after_reset is True
        assert cart_badge_qty_before_reset == '1'
        assert cart_badge_qty_after_reset == ''
