from chrome_browser import Browser
from pages import home_page, contul_meu_page, slowSearchBox_Page, contactMe_page


def before_all(context):
    context.chrome = Browser()
    context.homePage = home_page.HomePage()
    context.contulMeu = contul_meu_page.Login()
    context.ssb = slowSearchBox_Page.Ssb()
    context.contactMe = contactMe_page.Contact_me()


def after_all(context):
    context.chrome.close()