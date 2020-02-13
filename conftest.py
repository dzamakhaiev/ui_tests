import pytest
import pages
import test_data
from driver import ChromeDriver, EdgeDriver


@pytest.fixture(params=[ChromeDriver, EdgeDriver])
def start_page(request):
    # return start page for test case
    start_page = pages.MainPage(driver=request.param(), url=test_data.MAIN_PAGE)
    yield start_page

    # clean up a cart
    driver = start_page.get_driver()
    cart_page = pages.CartPage(driver=driver, url=test_data.CART_PAGE)
    cart_page.clean_cart()

    # quit from driver
    start_page.quit()

