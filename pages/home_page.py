from selenium.webdriver.common.by import By
from pages.base_page import Base_page

class HomePage(Base_page):
    EPNEU_LINK = (By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div/div[1]/h1/a/img')

    def site_acces(self):
        self.chrome.get('https://www.e-pneu.ro/')

    def logo_click(self):
        self.chrome.find_element(*self.EPNEU_LINK).click()

    def homepage_link_check(self):
        actual_url = self.chrome.current_url
        expected = 'https://www.e-pneu.ro/'
        self.assertEqual(expected, actual_url, 'expected link is not the same with actual URL')