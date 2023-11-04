from hw2.pages.base_page import BasePage
from hw2.locators.locators import CartPageLocators


class CartPage(BasePage):
    locators = CartPageLocators()

    def cart_items_list(self):
        return self.is_visible_all_elements(self.locators.CART_ITEMS_LIST)

    def cart_items_list_is_empty(self):
        return self.is_invisible(self.locators.CART_ITEMS_LIST)

    def cart_link(self):
        return self.is_visible(self.locators.CART_LINK)

    def cart_badge_qty(self):
        return self.is_visible(self.locators.CART_BADGE_QTY)

    def cart_badge_qty_is_absent(self):
        return self.is_invisible(self.locators.CART_BADGE_QTY)

    def item(self):
        return self.is_visible(self.locators.ITEM_NAME)

    def item_is_absent(self):
        return self.is_invisible(self.locators.ITEM_NAME)

    def item_name(self):
        return self.is_visible(self.locators.ITEM_NAME)

    def remove_button(self):
        return self.is_clickable(self.locators.REMOVE_BUTTON)

