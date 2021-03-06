from driver import BaseDriver
import locators


class BasePage:

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(BasePage, cls).__new__(cls)
        return cls.instance

    def __init__(self, driver, url):
        """
        :param BaseDriver driver: object for work with webdriver
        :param str url: base url for that page
        """
        self.driver = driver
        self.base_url = url
        self.driver.go_to(self.base_url)

    def get_driver(self):
        return self.driver

    def set_driver(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.get_current_url()

    def quit(self):
        self.driver.quit()


class MainPage(BasePage):

    def click_on_login_link(self):
        self.driver.click_on_element(locators.MainPageLocators.LOGIN_LINK)
        return self.driver

    def get_product_list(self):
        return self.driver.find_elements(locators.MainPageLocators.PRODUCT_BLOCK)

    def click_on_product(self, product):
        self.driver.click_on_element(locator=locators.MainPageLocators.PRODUCT_URL, element=product)

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


class ProductPage(BasePage):

    def add_product_to_cart(self):
        self.driver.click_on_element(locator=locators.ProductPage.BUY_BUTTON)


class CartPage(BasePage):

    def get_items_table(self):
        table = self.driver.find_element(locators.CartPageLocators.CART_TABLE)
        if not table: return []

        rows = self.driver.find_elements(locator=locators.CartPageLocators.CAR_ROW, element=table)
        if not rows: return []
        return rows[1:]

    def clean_cart(self):
        items_table = self.get_items_table()

        while len(items_table):
            links = self.driver.find_elements(locator=locators.CartPageLocators.DELETE_ITEM, element=items_table[-1])
            self.driver.click_on_element(element=links[-1])
            items_table = self.get_items_table()
