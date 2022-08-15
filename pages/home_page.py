from selenium.webdriver.common.by import By
from epneu.pages.base_page import Base_page

class Home_page(Base_page):
    EPNEU_LINK=(By.LINK_TEXT, 'Epneu Logo')

    def site_acces(self):
        self.chrome.get('https://www.e-pneu.ro/')

    def logo_click(self):
        self.chrome.find_element(*self.EPNEU_LINK).click()

    def homepage_link_check(self):
        actual_url=self.chrome.current_url
        expected='https://www.e-pneu.ro/'
        self.assertEqual(expected, actual_url, 'expected link is not the same with actual URL')