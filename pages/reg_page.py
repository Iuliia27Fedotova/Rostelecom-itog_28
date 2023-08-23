from pages.base import WebPage
from pages.elements import WebElement


class RegPage(WebPage):

    def __init__(self, web_driver):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    btn_checkin = WebElement(id='kc-register')
    password_reg = WebElement(id='password')
    password_reg_confirm = WebElement(id='password-confirm')
    btn_registration = WebElement(name='register')
    first_name = WebElement(name='firstName')
    last_name = WebElement(name='lastName')
    address = WebElement(id='address')
    msg = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
    page_confirm_email = WebElement(tag_name='h1')
    page_confirm_telefon = WebElement(tag_name='h1')
    page_reg = WebElement(tag_name='h1')
