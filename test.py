from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.implicitly_wait(5)
chrome.set_page_load_timeout(10)
chrome.maximize_window()
sleep(2)

chrome.get('https://www.e-pneu.ro/')

selection=chrome.find_element(By.XPATH, '//*[@id="1latime"]' ).click()
sleep(3)

# element=Select(chrome.find_element(By.ID, '1latime')).select_by_visible_text('235')


element=chrome.find_element(By.ID, '1latime')
sleep(3)
drp=Select(element).select_by_visible_text('235')
sleep(3)
element.click()
sleep(3)

chrome.quit()





