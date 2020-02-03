from selenium import webdriver


class BasePage:

    def __init__(self, driver):
        """
        :param webdriver.Chrome driver: added to help with auto fill
        """
        self.driver = driver

    def go_to(self, url):
        return self.driver.get(url=url)

    def find_element(self, by, value):
        return self.driver.find_element(by=by, value=value)

