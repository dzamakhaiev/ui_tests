from selenium.webdriver.common.by import By


# Main page
class MainPageLocators:
    LOGIN_LINK = (By.LINK_TEXT, 'Войти')
    PRODUCT_BLOCK = (By.CLASS_NAME, 'product-block')
    BUY_BUTTON = (By.TAG_NAME, 'input')
    CART_TOTAL = (By.ID, 'cart-total')


class LoginPageLocators:
    EMAIL_FIELD = (By.NAME, 'email')
    PWD_FIELD = (By.NAME, 'password')
    LOG_IN_BUTTON = (By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div/form/div/input[3]')
    USER_LINK = (By.XPATH, '//*[@id="header"]/div/div/div[3]/div[1]/a[1]')


class CartPageLocators:
    CART_TABLE = (By.CLASS_NAME, 'pav-shop-cart')
    CAR_ROW = (By.TAG_NAME, 'tr')
    DELETE_ITEM = (By.TAG_NAME, 'a')
