from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from time import sleep

class Contact_me(Base_page):
    contactMe_btn = (By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div/div[3]/div/span')
    nume = (By.XPATH, '//*[@id="exampleInputEmail1"]')
    telefon = (By.XPATH, '//*[@id="exampleInputEmail12"]')
    mail = (By.XPATH, '//*[@id="exampleInputEmail13"]')
    send_btn = (By.XPATH, '//*[@id="myModal"]/div/div/div[3]/button')

    def site_acces(self):
        self.chrome.get('https://www.e-pneu.ro/')
        sleep(1)
    def contact_btn(self):
        self.chrome.find_element(*self.contactMe_btn).click()
        sleep(1)
    def input_name(self):
        self.chrome.find_element(*self.nume).send_keys('Test Test')
        sleep(1)
    def input_phone(self):
        self.chrome.find_element(*self.telefon).send_keys('0123456789')
        sleep(1)
    def input_mail(self):
        self.chrome.find_element(*self.mail).send_keys('test@test.ro')
        sleep(1)
    def click_send(self):
        self.chrome.find_element(*self.send_btn).click()
        sleep(1)


