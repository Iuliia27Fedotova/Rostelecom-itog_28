from pages.base import WebPage
from pages.elements import WebElement


class ResetPage(WebPage):

    def __init__(self, web_driver):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    page_reset = WebElement(tag_name='h1')
    btn_reset_password = WebElement(id='forgot_password')
    tab_tel = WebElement(id='t-btn-tab-phone')
    tab_mail = WebElement(id='t-btn-tab-mail')
    tab_lc = WebElement(id='t-btn-tab-ls')
    tab_login = WebElement(id='t-btn-tab-login')
    btn_return = WebElement(id='reset-back')
    email_reset = WebElement(id='username')
    btn_continue = WebElement(id='reset')
    msg_reset = WebElement(id='form-error-message')
    page_auth = WebElement(tag_name='h1')
