from selenium import webdriver
from locators import *


class BasePage:

    def __init__(self, driver):
        """
        :param webdriver.Chrome driver: added to help with auto fill
        """
        self.driver = driver

    def go_to(self, url):
        return self.driver.get(url=url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        self.find_element(locator).click()

    def input_text(self, locator, text):
        field = self.find_element(locator)
        field.send_keys(text)


class MainPage(BasePage):

    def click_on_login_link(self):
        self.click_on_element(MainPageLocators.LOGIN_LINK)
        return self.driver


class LoginPage(BasePage):

    def log_in(self, email, password):
        self.input_text(locator=LoginPageLocators.EMAIL_FIELD, text=email)
        self.input_text(locator=LoginPageLocators.PWD_FIELD, text=password)
        self.click_on_element(LoginPageLocators.LOG_IN_BUTTON)


class AccountPage(BasePage):

    def get_user_name(self):
        return self.find_element(LoginPageLocators.USER_LINK).text
