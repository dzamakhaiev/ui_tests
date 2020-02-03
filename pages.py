import config
from selenium import webdriver


class BasePage:

    def __init__(self, driver_path=config.CHROMEDRIVER_PATH):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def __del__(self):
        self.driver.quit()
