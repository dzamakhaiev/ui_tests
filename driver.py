import config
from selenium import webdriver


class Driver:

    def __init__(self, driver_path=config.CHROMEDRIVER_PATH):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.implicitly_wait(config.IMP_WAIT_TIME)

    def __del__(self):
        self.driver.quit()
