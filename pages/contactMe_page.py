from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from time import sleep


class Contact_me(Base_page):
    contactMe_btn = (By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div/div[3]/div/span')
    nume = (By.ID, 'exampleInputEmail1')
    telefon = (By.ID, 'exampleInputEmail12')
    mail = (By.ID, 'exampleInputEmail13')
    send_btn = (By.NAME, 'trimite_solicitare_contact')

    def site_acces(self):
        self.chrome.get('https://www.e-pneu.ro/')

    def contact_btn(self):
        self.chrome.find_element(*self.contactMe_btn).click()

    def input_name(self):
        self.chrome.find_element(*self.nume).send_keys('Test Test')

    def input_phone(self):
        self.chrome.find_element(*self.telefon).send_keys('0123456789')

    def input_mail(self):
        self.chrome.find_element(*self.mail).send_keys('test@test.ro')

    def click_send(self):
        self.chrome.find_element(*self.send_btn).click()
        self.alerts_acceptance()



