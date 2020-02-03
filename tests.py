import unittest
from selenium import webdriver
import config
import test_data


class ChromeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=config.CHROMEDRIVER_PATH)
        self.driver.implicitly_wait(config.IMP_WAIT_TIME)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test(self):
        pass

    def test1(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
