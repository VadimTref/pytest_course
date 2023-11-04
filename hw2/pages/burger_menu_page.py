from hw2.pages.base_page import BasePage
from hw2.locators.locators import BurgerMenuLocators


class BurgerMenu(BasePage):
    locators = BurgerMenuLocators()

    def open_burger_menu(self):
        self.is_clickable(self.locators.LOGIN_BUTTON).click()
        error_message = self.is_visible(self.locators.ERROR_MESSAGE)

        return error_message.text
