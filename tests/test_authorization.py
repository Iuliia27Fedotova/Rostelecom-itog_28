from pages.auth_page import AuthPage
from settings import valid_email, valid_password, invalid_password, \
    invalid_email, valid_tel, invalid_tel, invalid_lc, invalid_login, valid_login, valid_lc
import pytest
from urllib.parse import urlparse


# RT-01 - Авторизация на сайте с помощью телефона существующего пользователя
def test_auth_tel_with_valid_data(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.email.send_keys(valid_tel)
    page.password.send_keys(valid_password)
    page.btn.click()
    page.wait_page_loaded()
    assert page.page_client.get_text() == 'Федотова'


# RT-02 - Авторизация на сайте с помощью телефона несуществующего пользователя
@pytest.mark.parametrize('telefon, password',
                         [(invalid_tel, valid_password),
                          (valid_tel, invalid_password),
                          (invalid_tel, invalid_password)],
                         ids=['invalid telefon', 'invalid password', 'invalid data'])
def test_auth_telefon_with_invalid_data(web_browser, telefon, password):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.email.send_keys(telefon)
    page.password.send_keys(password)
    page.btn.click()
    page.wait_page_loaded()
    assert page.page_auth.get_text() == 'Авторизация'
    assert page.msg.get_text() == 'Неверный логин или пароль'
    assert page.btn_reset_active.is_presented() is True


# RT-03 - Авторизация на сайте с помощью электронной почты существующего пользователя
def test_auth_email_with_valid_data(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_mail.click()
    page.email.send_keys(valid_email)
    page.password.send_keys(valid_password)
    page.btn.click()
    page.wait_page_loaded()
    assert page.page_client.get_text() == 'Федотова'


# RT-04 - Авторизация на сайте с помощью электронной почты несуществующего пользователя
@pytest.mark.parametrize('email, password',
                         [(invalid_email, valid_password),
                          (valid_email, invalid_password),
                          (invalid_email, invalid_password)],
                         ids=['invalid email', 'invalid password', 'invalid data'])
def test_auth_email_with_invalid_data(web_browser, email, password):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_mail.click()
    page.email.send_keys(email)
    page.password.send_keys(password)
    page.btn.click()
    page.wait_page_loaded()
    assert page.page_auth.get_text() == 'Авторизация'
    assert page.msg.get_text() == 'Неверный логин или пароль'
    assert page.btn_reset_active.is_presented() is True


# RT-05 - Авторизация на сайте с помощью логина существующего пользователя
def test_auth_login_with_valid_data(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_login.click()
    page.email.send_keys(valid_login)
    page.password.send_keys(valid_password)
    page.btn.click()
    page.wait_page_loaded()
    assert page.page_client.get_text() == 'Федотова'


# RT-06 - Авторизация на сайте с помощью логина несуществующего пользователя
@pytest.mark.parametrize('login, password',
                         [(invalid_login, valid_password),
                          (valid_login, invalid_password),
                          (invalid_login, invalid_password)],
                         ids=['invalid login', 'invalid password', 'invalid data'])
def test_auth_login_with_invalid_data(web_browser, login, password):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_login.click()
    page.email.send_keys(login)
    page.password.send_keys(password)
    page.btn.click()
    page.wait_page_loaded()
    assert page.page_auth.get_text() == 'Авторизация'
    assert page.msg.get_text() == 'Неверный логин или пароль'
    assert page.btn_reset_active.is_presented() is True


# RT-07 - Авторизация на сайте с помощью лицевого счета существующего пользователя
def test_auth_lc_with_valid_data(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_lc.click()
    page.email.send_keys(valid_lc)
    page.password.send_keys(valid_password)
    page.btn.click()
    page.wait_page_loaded()
    assert page.page_client.get_text() == 'Федотова'


# RT-08 - Авторизация на сайте с помощью лицевого счета несуществующего пользователя
@pytest.mark.parametrize('lc, password',
                         [(invalid_lc, valid_password),
                          (valid_lc, invalid_password),
                          (invalid_lc, invalid_password)],
                         ids=['invalid lc', 'invalid password', 'invalid data'])
def test_auth_lc_with_invalid_data(web_browser, lc, password):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.tab_lc.click()
    page.email.send_keys(lc)
    page.password.send_keys(password)
    page.btn.click()
    page.wait_page_loaded()
    assert page.page_auth.get_text() == 'Авторизация'
    assert page.msg.get_text() == 'Неверный логин или пароль'
    assert page.btn_reset_active.is_presented() is True


# RT-09 - Работа кнопки "Забыл пароль"
def test_btn_reset_password(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.btn_reset_password.click()
    page.wait_page_loaded()
    assert page.page_reset.get_text() == "Восстановление пароля"


# RT-10 - Работа кнопки "Зарегистрироваться"
def test_btn_checkin(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.btn_checkin.click()
    page.wait_page_loaded()
    assert page.page_reg.get_text() == "Регистрация"


# RT-11 - Авторизация с помощью соц. сети - ВКонтакте
def test_auth_vk(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.vk_icon.click()
    page.wait_page_loaded()
    assert urlparse(web_browser.current_url).netloc == 'id.vk.com'


# RT-12 - Авторизация с помощью соц. сети - Одноклассники
def test_auth_ok(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.ok_icon.click()
    page.wait_page_loaded()
    assert urlparse(web_browser.current_url).netloc == 'connect.ok.ru'


# RT-13 - Авторизация с помощью соц. сети - Mail
def test_auth_mail(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.mail_icon.click()
    page.wait_page_loaded()
    assert urlparse(web_browser.current_url).netloc == 'connect.mail.ru'


# RT-14 - Авторизация с помощью соц. сети - Яндекс
def test_auth_yandex(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.yandex_icon.click()
    page.wait_page_loaded()
    assert urlparse(web_browser.current_url).netloc == 'passport.yandex.ru'


# RT-24 - Тестирование работы автоматического переключения таба
@pytest.mark.parametrize('tab',
                         [valid_tel, valid_email, valid_login, valid_lc],
                         ids=['tab_tel', 'tab_email', 'tab_login', 'tab_ls'])
def test_automatic_work_tab(web_browser, tab):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.email.send_keys(tab)
    page.password.click()
    page.wait_page_loaded()
    if tab == valid_tel:
        assert page.tab_active.get_text() == page.tab_tel.get_text()
    if tab == valid_email:
        assert page.tab_active.get_text() == page.tab_mail.get_text()
    if tab == valid_login:
        assert page.tab_active.get_text() == page.tab_login.get_text()
    if tab == valid_lc:
        assert page.tab_active.get_text() == page.tab_lc.get_text()
