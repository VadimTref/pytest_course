from hw2.data.data import LOGIN, PASSWORD, FAKE_LOGIN, FAKE_PASSWORD
from hw2.pages.base_page import BasePage
from hw2.locators.locators import LoginPageLocators


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def login_standard_user(self):
        self.is_visible(self.locators.USERNAME_FIELD).send_keys(LOGIN)
        self.is_visible(self.locators. PASSWORD_FIELD).send_keys(PASSWORD)
        self.is_clickable(self.locators.LOGIN_BUTTON).click()

    def login_fake_user(self):
        self.is_visible(self.locators.USERNAME_FIELD).send_keys(FAKE_LOGIN)
        self.is_visible(self.locators. PASSWORD_FIELD).send_keys(FAKE_PASSWORD)
        self.is_clickable(self.locators.LOGIN_BUTTON).click()
        error_message = self.is_visible(self.locators.ERROR_MESSAGE)

        return error_message.text

    def login_parametrize_user(self, login, password):
        self.is_visible(self.locators.USERNAME_FIELD).send_keys(login)
        self.is_visible(self.locators. PASSWORD_FIELD).send_keys(password)
        self.is_clickable(self.locators.LOGIN_BUTTON).click()

    def login_parametrize_fake_user(self, login, password):
        self.is_visible(self.locators.USERNAME_FIELD).send_keys(login)
        self.is_visible(self.locators. PASSWORD_FIELD).send_keys(password)
        self.is_clickable(self.locators.LOGIN_BUTTON).click()
        error_message = self.is_visible(self.locators.ERROR_MESSAGE)

        return error_message.text
