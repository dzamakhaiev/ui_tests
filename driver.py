from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome
import config


class BaseDriver:

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

    def find_element(self, locator, element=None):
        """
        :param tuple locator:
        :param WebElement element:
        """
        if not element:
            return self.driver.find_element(*locator)
        else:
            return element.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_on_element(self, locator, element=None):
        self.find_element(locator, element).click()

    def input_text(self, locator, text, element=None):
        field = self.find_element(locator, element)
        field.send_keys(text)

    def __del__(self):
        # Cannot use here quit() due to issue: https://github.com/SeleniumHQ/selenium/issues/3330
        self.driver.close()


class ChromeDriver(BaseDriver):

    def __init__(self, driver_path=config.CHROMEDRIVER_PATH):
        driver = Chrome(executable_path=driver_path)
        super().__init__(driver)

