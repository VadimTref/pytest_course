from hw2.pages.base_page import BasePage
from hw2.locators.locators import SauceLabsPageLocators


class SauceLabsPage(BasePage):
    locators = SauceLabsPageLocators()

    def sauce_labs_logo(self):
        return self.is_visible(self.locators.SAUCE_LABS_LOGO)

    def sauce_labs_text(self):
        return self.is_visible(self.locators.TEXT).text

