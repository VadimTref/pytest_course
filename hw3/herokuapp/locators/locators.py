from selenium.webdriver.common.by import By

ADD_BUTTON = (By.XPATH, "//button[contains(text(),'Add Element')]")
DELETE_BUTTON = (By.CSS_SELECTOR, '#elements > button:nth-child(1)')
DELETE_BUTTON_LIST = (By.CSS_SELECTOR, '#elements > button')