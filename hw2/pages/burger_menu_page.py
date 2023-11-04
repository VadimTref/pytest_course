from hw2.pages.base_page import BasePage
from hw2.locators.locators import BurgerMenuLocators


class BurgerMenuPage(BasePage):
    locators = BurgerMenuLocators()

    def open_burger_menu(self):
        self.is_clickable(self.locators.BURGER_MENU_LINK).click()
        burger_menu_field = self.is_visible(self.locators.BURGER_MENU_FIELD)
        assert burger_menu_field.is_displayed()

    def logout_button(self):
        return self.is_clickable(self.locators.LOGOUT_BUTTON)

    def about_button(self):
        return self.is_clickable(self.locators.ABOUT_BUTTON)

    def reset_app_state_button(self):
        return self.is_clickable(self.locators.RESET_APP_STATE_BUTTON)

    def close_burger_menu(self):
        self.is_clickable(self.locators.CLOSE_BURGER_MENU).click()
        self.driver.refresh()
