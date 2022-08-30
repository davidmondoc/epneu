from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from time import sleep
from selenium.webdriver.support.ui import Select

class Ssb(Base_page):
    tireType = (By.ID, 'tab_auto')
    tireWidth = (By.ID, '1latime')
    tireHeight = (By.ID, '1inaltime')
    tireDiameter = (By.ID, '1diametru')
    tireProducer = (By.ID,'1brand' )
    tireSeason = (By.ID, '1sezon')
    srcBtn = (By.XPATH, '//*[@id="cauta-anvelope-auto"]')


    def site_acces(self):
        self.chrome.get('https://www.e-pneu.ro/')

    def tiretype_src(self):
        self.chrome.find_element(*self.tireType).click()

    def width(self):
        self.chrome.find_element(*self.tireWidth).click()
        element = Select(self.chrome.find_element(*self.tireWidth))
        element.select_by_visible_text('235')

    def height(self):
        self.chrome.find_element(*self.tireHeight).click()
        element = Select(self.chrome.find_element(*self.tireHeight))
        element.select_by_visible_text('45')

    def diameter(self):
        self.chrome.find_element(*self.tireDiameter).click()
        element = Select(self.chrome.find_element(*self.tireDiameter))
        element.select_by_visible_text('17')

    def producer(self):
        self.chrome.find_element(*self.tireProducer).click()
        element = Select(self.chrome.find_element(*self.tireProducer))
        element.select_by_visible_text('FALKEN')

    def season(self):
        self.chrome.find_element(*self.tireSeason).click()
        element = Select(self.chrome.find_element(*self.tireSeason))
        element.select_by_visible_text('Iarna')

    def clicksrc(self):
        self.chrome.find_element(*self.srcBtn).click()



