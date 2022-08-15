from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase
from chrome_browser import Browser


class Base_page(Browser, TestCase):
    def wait_for_elem_by_selector(self , by , selector):
        WebDriverWait( self.chrome, 5 ).until(EC.presence_of_element_located((by, selector)))