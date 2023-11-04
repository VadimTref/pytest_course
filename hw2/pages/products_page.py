from hw2.pages.base_page import BasePage
from hw2.locators.locators import ProductsPageLocators


class ProductsPage(BasePage):
    locators = ProductsPageLocators()

    def add_to_cart_button(self):
        return self.is_clickable(self.locators.ADD_TO_CART_BUTTON)

    def cart_link(self):
        return self.is_clickable(self.locators.CART_LINK)

    def item_name(self):
        return self.is_clickable(self.locators.ITEM_NAME)


