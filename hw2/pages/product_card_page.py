from hw2.pages.base_page import BasePage
from hw2.locators.locators import ProductCardPageLocators


class ProductCardPage(BasePage):
    locators = ProductCardPageLocators()

    def add_to_cart_button(self):
        return self.is_clickable(self.locators.ADD_TO_CART_BUTTON)

    def cart_link(self):
        return self.is_clickable(self.locators.CART_LINK)

    def cart_badge_qty(self):
        return self.is_visible(self.locators.CART_BADGE_QTY)

    def remove_button(self):
        return self.is_clickable(self.locators.REMOVE_BUTTON)

