from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD = (By.XPATH, '//input[@data-test="username"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@data-test="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@data-test="login-button"]')
    ERROR_MESSAGE = (By.XPATH, '//h3')


class BurgerMenuLocators:
    BURGER_MENU_LINK = (By.CSS_SELECTOR, '#react-burger-menu-btn')
    BURGER_MENU_FIELD = (By.CSS_SELECTOR, '.bm-menu')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '#logout_sidebar_link')
    ABOUT_BUTTON = (By.CSS_SELECTOR, '#about_sidebar_link')
    RESET_APP_STATE_BUTTON = (By.CSS_SELECTOR, '#reset_sidebar_link')
    CLOSE_BURGER_MENU = (By.CSS_SELECTOR, '#react-burger-cross-btn')


class SauceLabsPageLocators:
    SAUCE_LABS_LOGO = (By.XPATH, '//img[@src="/images/logo.svg"]')
    TEXT = (By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-body1.css-sere2z')


class ProductsPageLocators:
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
    CART_LINK = (By.CSS_SELECTOR, '.shopping_cart_link')
    ITEM_NAME = (By.CSS_SELECTOR, '#item_4_title_link > div')


class CartPageLocators:
    CART_ITEMS_LIST = (By.CSS_SELECTOR, '.cart_item')
    CART_LINK = (By.CSS_SELECTOR, '.shopping_cart_link')
    CART_BADGE_QTY = (By.XPATH, '//span[@class="shopping_cart_badge"]')
    ITEM = (By.CLASS_NAME, 'cart_item')
    ITEM_NAME = (By.CSS_SELECTOR, '#item_4_title_link > div')
    REMOVE_BUTTON = (By.XPATH, '//button[@id="remove-sauce-labs-backpack"]')


class ProductCardPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_BADGE_QTY = (By.XPATH, '//span[@class="shopping_cart_badge"]')
    REMOVE_BUTTON = (By.XPATH, '//button[@id="remove-sauce-labs-backpack"]')

