from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Chrome
import config


class Driver:

    def __init__(self, driver):
        """
        :param WebDriver driver:
        """
        self.driver = driver
        self.driver.implicitly_wait(config.IMP_WAIT_TIME)
        self.driver.maximize_window()

    def __del__(self):
        # Cannot use here quit() due to issue: https://github.com/SeleniumHQ/selenium/issues/3330
        self.driver.close()


class ChromeDriver(Driver):

    def __init__(self, driver_path=config.CHROMEDRIVER_PATH):
        driver = Chrome(executable_path=driver_path)
        super().__init__(driver)

