from pages.reset_page import ResetPage
from settings import valid_email, valid_tel, valid_login, valid_lc


# RT-15 - Восстановление пароля по номеру телефона без ввода капчи
def test_reset_password_tel_negativ(web_browser):
    page = ResetPage(web_browser)
    page.btn_reset_password.click()
    page.wait_page_loaded()
    assert page.page_reset.get_text() == "Восстановление пароля"
    page.email_reset.send_keys(valid_tel)
    page.btn_continue.click()
    page.wait_page_loaded()
    assert page.msg_reset.get_text() == 'Неверный логин или текст с картинки'


# RT-16 - Восстановление пароля по электронной почте без ввода капчи
def test_reset_password_email_negativ(web_browser):
    page = ResetPage(web_browser)
    page.btn_reset_password.click()
    page.wait_page_loaded()
    assert page.page_reset.get_text() == "Восстановление пароля"
    page.tab_mail.click()
    page.email_reset.send_keys(valid_email)
    page.btn_continue.click()
    page.wait_page_loaded()
    assert page.msg_reset.get_text() == 'Неверный логин или текст с картинки'


# RT-17 - Восстановление пароля по логину без ввода капчи
def test_reset_password_login_negativ(web_browser):
    page = ResetPage(web_browser)
    page.btn_reset_password.click()
    page.wait_page_loaded()
    assert page.page_reset.get_text() == "Восстановление пароля"
    page.tab_login.click()
    page.email_reset.send_keys(valid_login)
    page.btn_continue.click()
    page.wait_page_loaded()
    assert page.msg_reset.get_text() == 'Неверный логин или текст с картинки'


# RT-18 - Восстановление пароля по лицевому счету без ввода капчи
def test_reset_password_ls_negativ(web_browser):
    page = ResetPage(web_browser)
    page.btn_reset_password.click()
    page.wait_page_loaded()
    assert page.page_reset.get_text() == "Восстановление пароля"
    page.tab_lc.click()
    page.email_reset.send_keys(valid_lc)
    page.btn_continue.click()
    page.wait_page_loaded()
    assert page.msg_reset.get_text() == 'Неверный логин или текст с картинки'


# RT-19 - Кнопка "Вернуться назад" на странице "Восстановление пароля"
def test_btn_return(web_browser):
    page = ResetPage(web_browser)
    page.btn_reset_password.click()
    page.wait_page_loaded()
    assert page.page_reset.get_text() == "Восстановление пароля"
    page.btn_return.click()
    page.wait_page_loaded()
    assert page.page_auth.get_text() == 'Авторизация'
