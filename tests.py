import random
import unittest
import pages
import test_data
from driver import ChromeDriver


class ChromeTest(unittest.TestCase):

    def setUp(self):
        # Start test case from Main page like regular user
        self.current_page = pages.MainPage(driver=ChromeDriver(), url=test_data.MAIN_PAGE)

    def tearDown(self):
        # Clean a cart
        driver = self.current_page.get_driver()
        cart_page = pages.CartPage(driver=driver, url=test_data.CART_PAGE)
        cart_page.clean_cart()
        self.current_page = cart_page

        self.current_page.quit()

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

    @staticmethod
    def format_product_desc(product_desc):
        """
        :param str product_desc: line with product description
        """
        parts = product_desc.split('\n')
        price = parts[-1].split(' ')
        price = ''.join([p for p in price[:-1]])
        desc = [p for p in parts if test_data.PRODUCT_MARKER in p and test_data.IGNORE_MARKER not in p][0]

        return desc, float(price)

    @staticmethod
    def format_cart_total(cart_total):
        """
        :param str cart_total: string with number of products and total price
        """
        cart_total = cart_total.replace('(', '').replace(')', '')
        cart_total = cart_total.split(' ')
        cart_total = cart_total[1:-1]
        number = cart_total.pop(0)
        price = ''.join(digits for digits in cart_total)
        return int(number), float(price)

    def check_product_in_cart(self, items, product_desc):
        """
        :param list items:
        :param str product_desc:
        """
        product_desc, _ = self.format_product_desc(product_desc)

        for item in items:
            if product_desc in item.text:
                break
        else:
            self.fail(f'Product {product_desc} not found in cart items')

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

    def test_add_product_to_cart(self):
        # Start from Main page and log in
        self.log_in()

        # Turn back to main page
        driver = self.current_page.get_driver()
        main_page = pages.MainPage(driver=driver, url=test_data.MAIN_PAGE)

        # Pick up random product
        products = main_page.get_product_list()
        product = random.choice(products)
        product_desc = product.text

        # Try to add product to cart
        main_page.add_product_to_cart(product)

        # Check cart
        driver = main_page.get_driver()
        cart_page = pages.CartPage(driver=driver, url=test_data.CART_PAGE)
        self.current_page = cart_page
        items = cart_page.get_items_table()
        self.check_product_in_cart(items=items, product_desc=product_desc)

    def test_add_products_to_cart(self):
        # Start from Main page and log in
        self.log_in()

        # Turn back to main page
        driver = self.current_page.get_driver()
        main_page = pages.MainPage(driver=driver, url=test_data.MAIN_PAGE)

        # Pick up few random products and try to add them  into cart
        count = 0
        exp_total = 0.0
        number_of_products = 10
        products = main_page.get_product_list()

        for i in range(random.randint(1, number_of_products)):
            product = random.choice(products)
            main_page.add_product_to_cart(product)
            desc, price = self.format_product_desc(product.text)
            count += 1
            exp_total += price

        # Check number of products and total price
        cart_total = main_page.get_cart_total()
        number, act_total = self.format_cart_total(cart_total)
        self.assertEqual(count, number)
        self.assertEqual(act_total, exp_total)


if __name__ == '__main__':
    unittest.main(verbosity=2)
