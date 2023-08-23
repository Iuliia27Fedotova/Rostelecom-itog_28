from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    page_auth = WebElement(tag_name='h1')
    page_reset = WebElement(tag_name='h1')
    page_reg = WebElement(tag_name='h1')
    page_client = WebElement(css_selector='span.user-name__last-name')
    email = WebElement(id='username')
    password = WebElement(id='password')
    btn = WebElement(id='kc-login')
    vk_icon = WebElement(id='oidc_vk')
    ok_icon = WebElement(id='oidc_ok')
    mail_icon = WebElement(id='oidc_mail')
    yandex_icon = WebElement(id='oidc_ya')
    btn_checkin = WebElement(id='kc-register')
    btn_reset_password = WebElement(id='forgot_password')
    tab_tel = WebElement(id='t-btn-tab-phone')
    tab_mail = WebElement(id='t-btn-tab-mail')
    tab_lc = WebElement(id='t-btn-tab-ls')
    tab_login = WebElement(id='t-btn-tab-login')
    tab_active = WebElement(class_name='rt-tab--active')
    captcha = WebElement(id='captcha')
    msg = WebElement(id='form-error-message')
    btn_reset_active = WebElement(class_name='login-form__forgot-pwd--animated')
