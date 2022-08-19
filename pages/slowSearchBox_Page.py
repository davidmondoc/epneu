from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from time import sleep
from selenium.webdriver.support.ui import Select

class Ssb(Base_page):
    tireType = (By.ID, 'tab_auto')
    tireWidth = (By.ID, '1latime')
    tireHeight = (By.ID, )
    tireDiameter = (By.ID, )
    tireProducer = (By.ID, )
    tireSeason = (By.ID, )
    srcBtn = (By.XPATH, '//*[@id="cauta-anvelope-auto"]')


    def site_acces(self):
        self.chrome.get('https://www.e-pneu.ro/')

    def tiretype_src(self):
        self.chrome.find_element(*self.tireType).click()
        sleep(5)

    def tirewidth(self):
        element=Select(self.chrome.find_element(*self.tireWidth))
        element.select_by_visible_text('235')
        sleep(5)

    def clicksrc(self):
        self.chrome.find_element(*self.srcBtn).click()
        sleep(3)
'''
    def tireheight(self):
        self.chrome.find_element(*self.tireHeight)

    def tirediameter(self):
        self.chrome.find_element(*self.tireDiameter)

    def tireproducer(self):
        self.chrome.find_element(*self.tireProducer)

    def tireseason(self):
        self.chrome.find_element(*self.tireSeason)

    def clicksrc(self):
        self.chrome.find_element(*self.srcBtn).click()
'''


