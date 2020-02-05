import unittest
import random
from driver import ChromeDriver
import test_data
import pages


class ChromeTest(unittest.TestCase):

    def setUp(self):
        # Start test case from Main page like regular user
        self.current_page = pages.MainPage(driver=ChromeDriver(), url=test_data.MAIN_PAGE)

    def log_in(self):
        # Start from Main page
        driver = self.current_page.get_driver()
        main_page = pages.MainPage(driver=driver, url=test_data.MAIN_PAGE)
        main_page.click_on_login_link()

        # Go to login page
        driver = self.current_page.get_driver()
        login_page = pages.LoginPage(driver=driver, url=test_data.LOGIN_PAGE)
        login_page.log_in(email=test_data.USER_EMAIL, password=test_data.USER_PWD)

        # After log in current page will be Account page
        driver = self.current_page.get_driver()
        self.current_page = pages.AccountPage(driver=driver, url=test_data.ACCOUNT_PAGE)

    def test_login(self):
        # Start from Main page and log in to reach Account page
        self.log_in()

        # Check current page after log in
        self.assertEqual(self.current_page.get_current_url(), test_data.ACCOUNT_PAGE)

        # Check user name after log in
        driver = self.current_page.get_driver()
        acc_page = pages.AccountPage(driver=driver, url=test_data.ACCOUNT_PAGE)
        user_name = acc_page.get_user_name()
        self.assertEqual(user_name, test_data.USER_NAME)

    def test_add_to_cart(self):
        # Start from Main page and log in
        self.log_in()

        # Turn back to main page
        driver = self.current_page.get_driver()
        main_page = pages.MainPage(driver=driver, url=test_data.MAIN_PAGE)

        # Pick up random product
        products = main_page.get_product_list()
        product = random.choice(products)

        # Try to add product to cart
        main_page.add_product_to_cart(product)

        # Check cart


if __name__ == '__main__':
    unittest.main(verbosity=2)
