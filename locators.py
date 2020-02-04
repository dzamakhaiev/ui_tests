from selenium.webdriver.common.by import By


# Main page
class MainPageLocators:
    LOGIN_LINK = (By.LINK_TEXT, 'Войти')


class LoginPageLocators:
    EMAIL_FIELD = (By.NAME, 'email')
    PWD_FIELD = (By.NAME, 'password')
    LOG_IN_BUTTON = (By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div/form/div/input[3]')
    USER_LINK = (By.XPATH, '//*[@id="header"]/div/div/div[3]/div[1]/a[1]')