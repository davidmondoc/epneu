from selenium.webdriver.common.by import By
from pages.base_page import Base_page


class Login(Base_page):
    ACCOUNT_PAGE = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/div[4]/div[2]/a')
    USER = (By.XPATH, '//*[@id="email"]')
    PASSWORD = (By.XPATH, '//*[@id="pass"]')
    FORGOT_PASS = (By.LINK_TEXT, 'Ai uitat parola?')
    GO_BACK = (By.XPATH, '//*[@id="form-validate"]/div[2]/p[2]/a')
    ERRORMSG = (By.XPATH, '//*[@id="advice-required-entry-pass"]')
    AUTENTIFICARE = (By.XPATH, '//*[@id="send2"]')

    def site_acces(self):
        self.chrome.get('https://www.e-pneu.ro/')

    def account_page(self):
        self.chrome.find_element(*self.ACCOUNT_PAGE).click()

    def user(self):
        self.chrome.find_element(*self.USER).send_keys('test@test.com')

    def password(self):
        self.chrome.find_element(*self.PASSWORD).send_keys('parola123')

    def forgot_pass(self):
        self.chrome.find_element(*self.FORGOT_PASS).click()

    def go_back(self):
        self.chrome.find_element(*self.GO_BACK).click()

    def autentificare(self):
        self.chrome.find_element(*self.AUTENTIFICARE).click()

    def errormsg(self):
        self.chrome.find_element(*self.ERRORMSG).is_displayed()


