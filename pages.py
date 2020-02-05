from driver import Driver
import locators


class BasePage:

    def __init__(self, driver, url):
        """
        :param Driver driver: object for work with webdriver
        :param str url: base url for that page
        """
        self.driver = driver
        self.base_url = url


class MainPage(BasePage):

    def click_on_login_link(self):
        self.driver.click_on_element(locators.MainPageLocators.LOGIN_LINK)
        return self.driver

    def get_product_list(self):
        return self.driver.find_elements(locators.MainPageLocators.PRODUCT_BLOCK)

    def add_product_to_cart(self, product):
        self.driver.click_on_element(locator=locators.MainPageLocators.BUY_BUTTON, element=product)

    def get_cart_total(self):
        return self.driver.find_element(locators.MainPageLocators.CART_TOTAL).text


class LoginPage(BasePage):

    def log_in(self, email, password):
        self.driver.input_text(locator=locators.LoginPageLocators.EMAIL_FIELD, text=email)
        self.driver.input_text(locator=locators.LoginPageLocators.PWD_FIELD, text=password)
        self.driver.click_on_element(locators.LoginPageLocators.LOG_IN_BUTTON)


class AccountPage(BasePage):

    def get_user_name(self):
        return self.driver.find_element(locators.LoginPageLocators.USER_LINK).text


class CartPage(BasePage):
    pass
