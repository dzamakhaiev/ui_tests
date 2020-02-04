import unittest
from selenium import webdriver
import config
import test_data
import pages


class ChromeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=config.CHROMEDRIVER_PATH)
        self.driver.implicitly_wait(config.IMP_WAIT_TIME)
        self.driver.maximize_window()
        self.driver.get(url=test_data.MAIN_PAGE)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Start from Main page
        main_page = pages.MainPage(driver=self.driver)
        main_page.click_on_login_link()

        # Go to login page
        login_page = pages.LoginPage(self.driver)
        login_page.log_in(email=test_data.USER_EMAIL, password=test_data.USER_PWD)

        # Check current page after log in
        self.assertEqual(self.driver.current_url, test_data.ACCOUNT_PAGE)

        # Check user name after log in
        acc_page = pages.AccountPage(self.driver)
        user_name = acc_page.get_user_name()
        self.assertEqual(user_name, test_data.USER_NAME)

    def test1(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
