from hw2.data.data import PRODUCTS_PAGE_URL, CART_PAGE_URL, PRODUCT_CARD_PAGE_URL
from hw2.pages.products_page import ProductsPage
from hw2.pages.cart_page import CartPage
from hw2.pages.product_card_page import ProductCardPage


class TestCart:
    def test_add_item_to_cart_from_catalog(self, driver, login_standard_user):
        page = ProductsPage(driver, PRODUCTS_PAGE_URL)
        page.add_to_cart_button().click()
        page.cart_link().click()

        page = CartPage(driver, CART_PAGE_URL)
        item_name = page.item_name().text

        assert driver.current_url == CART_PAGE_URL
        assert item_name == 'Sauce Labs Backpack'

    def test_remove_item_from_cart_through_cart(self, driver, login_standard_user):
        page = ProductsPage(driver, PRODUCTS_PAGE_URL)
        page.add_to_cart_button().click()
        page.cart_link().click()

        page = CartPage(driver, CART_PAGE_URL)
        item = page.item()

        assert item.is_displayed()

        qty_of_items_in_cart_badge = page.cart_link()

        qty_of_items_in_cart_badge_before_remove = qty_of_items_in_cart_badge.text
        cart_badge_qty_before_remove = page.cart_badge_qty()

        page.remove_button().click()

        item_is_absent = page.item_is_absent()
        qty_of_items_in_cart_badge_after_remove = qty_of_items_in_cart_badge.text
        cart_badge_qty_after_remove = page.cart_badge_qty_is_absent()

        assert item_is_absent is True
        assert qty_of_items_in_cart_badge_before_remove == '1'
        assert qty_of_items_in_cart_badge_after_remove == ''
        assert cart_badge_qty_before_remove is not None
        assert cart_badge_qty_after_remove is True

    def test_add_item_to_cart_from_product_card(self, driver, login_standard_user):
        page = ProductsPage(driver, PRODUCTS_PAGE_URL)
        page.item_name().click()

        assert driver.current_url == PRODUCT_CARD_PAGE_URL

        page = ProductCardPage(driver, PRODUCT_CARD_PAGE_URL)
        page.add_to_cart_button().click()
        page.cart_link().click()

        page = CartPage(driver, CART_PAGE_URL)
        item_name = page.item_name()

        assert driver.current_url == CART_PAGE_URL
        assert item_name.text == 'Sauce Labs Backpack'

    def test_remove_item_from_cart_through_item_card(self, driver, login_standard_user):
        page = ProductsPage(driver, PRODUCTS_PAGE_URL)
        page.item_name().click()

        assert driver.current_url == PRODUCT_CARD_PAGE_URL

        page = ProductCardPage(driver, PRODUCT_CARD_PAGE_URL)
        page.add_to_cart_button().click()
        page.cart_link().click()

        page = CartPage(driver, CART_PAGE_URL)

        assert page.item().is_displayed()

        item_is_visible_before_remove = page.item()
        qty_of_items_in_cart_badge_before_remove = page.cart_link().text
        cart_badge_qty_visible_before_remove = page.cart_badge_qty()

        driver.back()

        page = ProductCardPage(driver, PRODUCT_CARD_PAGE_URL)
        page.remove_button().click()
        page.cart_link().click()

        page = CartPage(driver, CART_PAGE_URL)
        qty_of_items_in_cart_badge_after_remove = page.cart_link().text
        cart_badge_qty_invisible_after_remove = page.cart_badge_qty_is_absent()
        item_is_invisible_after_remove = page.item_is_absent()

        assert qty_of_items_in_cart_badge_before_remove == '1'
        assert qty_of_items_in_cart_badge_after_remove == ''
        assert cart_badge_qty_visible_before_remove is not None
        assert cart_badge_qty_invisible_after_remove is True
        assert item_is_visible_before_remove is not None
        assert item_is_invisible_after_remove is True
