from selenium.webdriver.common.by import By
from pages.base_page import Base_page


class HomePage(Base_page):
    EPNEU_LINK = (By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div/div[1]/a/img')
    SEARCH_FIELD = (By.ID, 'search1')
    SEARCH_BTN = (By.CLASS_NAME, 'button')
    ALL_SEASON = (By.XPATH, '//*[@id="narrow-by-list-0"]/dd[2]/ol/li[1]/a')

    def site_acces(self):
        self.chrome.get('https://www.e-pneu.ro/')

    def search_field(self):
        self.chrome.find_element(*self.SEARCH_FIELD).send_keys('2354517')

    def search_btn(self):
        self.chrome.find_element(*self.SEARCH_BTN).click()

    def all_season_selection(self):
        self.chrome.find_element(*self.ALL_SEASON).click()

    def logo_click(self):
        self.chrome.find_element(*self.EPNEU_LINK).click()

    def homepage_link_check(self):
        actual_url = self.chrome.current_url
        expected = 'https://www.e-pneu.ro/'
        self.assertEqual(expected, actual_url, 'expected link is not the same with actual URL')