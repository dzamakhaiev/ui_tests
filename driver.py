from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome, Edge
from selenium.common.exceptions import NoSuchElementException

import config


def no_such_element_exception(find):
    def wrap(self, *args, **kwargs):
        try:
            return find(self, *args, **kwargs)
        except NoSuchElementException:
            return None
    return wrap


def no_such_elements_exception(find):
    def wrap(self, *args, **kwargs):
        try:
            return find(self, *args, **kwargs)
        except NoSuchElementException:
            return []
    return wrap


class BaseDriver:

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(BaseDriver, cls).__new__(cls)
        return cls.instance

    def __init__(self, driver):
        """
        :param WebDriver driver:
        """
        self.driver = driver
        self.driver.implicitly_wait(config.IMP_WAIT_TIME)
        self.driver.maximize_window()

    def get_driver(self):
        return self.driver

    def set_driver(self, driver):
        """
        :param WebDriver driver:
        """
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    @no_such_element_exception
    def find_element(self, locator, element=None):
        """
        :param tuple locator:
        :param WebElement element:
        """
        if not element:
            return self.driver.find_element(*locator)
        else:
            return element.find_element(*locator)

    @no_such_elements_exception
    def find_elements(self, locator, element=None):
        """
        :param tuple locator:
        :param WebElement element:
        """
        if not element:
            return self.driver.find_elements(*locator)
        else:
            return element.find_elements(*locator)

    def click_on_element(self, locator=None, element=None):
        """
        :param tuple locator:
        :param WebElement element:
        """
        if not locator and element:
            element.click()
        else:
            self.find_element(locator, element).click()

        sleep(config.CALCULATING_TIME)  # when simple wait does not help and web app has low performance

    def input_text(self, locator, text, element=None):
        field = self.find_element(locator, element)
        field.send_keys(text)

    def quit(self):
        self.driver.quit()


class ChromeDriver(BaseDriver):

    def __init__(self, driver_path=config.CHROMEDRIVER_PATH):
        driver = Chrome(executable_path=driver_path)
        super().__init__(driver)


class EdgeDriver(BaseDriver):

    def __init__(self):
        driver = Edge()
        super().__init__(driver)
