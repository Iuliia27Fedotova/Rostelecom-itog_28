from pages.reg_page import RegPage
import pytest


def generate_rus_string(num):
    """Генерация строки на кириллице"""
    return "я" * num


def generate_eng_string(num):
    """Генерация строки на латинице"""
    return "h" * num


def generate_spec_string(num):
    """Генерация строки из спецсимволов"""
    return "@" * num


def generate_num_string(num):
    """Генерация строки из цифр"""
    return "3" * num


# RT-20 - Регистрация нового пользователя на сайте с помощью email
def test_checkin_email_with_valid_data(web_browser):
    page = RegPage(web_browser)
    page.wait_page_loaded()
    page.btn_checkin.click()
    assert page.page_reg.get_text() == "Регистрация"
    page.first_name.send_keys("Полина")
    page.last_name.send_keys("Иванова")
    page.address.send_keys('juliaa-15@mail.ru')
    page.password_reg.send_keys('Ju123456')
    page.password_reg_confirm.send_keys('Ju123456')
    page.btn_registration.click()
    page.wait_page_loaded()
    assert page.page_confirm_email.get_text() == "Подтверждение email"


# RT-21 - Регистрация нового пользователя на сайте с помощью телефона
def test_checkin_tel_with_valid_data(web_browser):
    page = RegPage(web_browser)
    page.btn_checkin.click()
    page.wait_page_loaded()
    assert page.page_reg.get_text() == "Регистрация"
    page.first_name.send_keys("Полина")
    page.last_name.send_keys("Иванова")
    page.address.send_keys('89221699966')
    page.password_reg.send_keys('Ju123456')
    page.password_reg_confirm.send_keys('Ju123456')
    page.btn_registration.click()
    page.wait_page_loaded()
    assert page.page_confirm_telefon.get_text() == "Подтверждение телефона"


# RT-22 - Ввод имени, вводимого при регистрации, не соответствующего требованиям
@pytest.mark.parametrize('name_reg', ['', generate_rus_string(1), generate_rus_string(35),
                                      generate_eng_string(1), generate_eng_string(2), generate_eng_string(15), generate_eng_string(30), generate_eng_string(35),
                                      generate_spec_string(1), generate_spec_string(2), generate_spec_string(15), generate_spec_string(30), generate_spec_string(35),
                                      generate_num_string(1), generate_num_string(2), generate_num_string(15), generate_num_string(30), generate_num_string(35)],
                         ids=['clear', '1 russian symbol', '35 russian symbol',
                              '1 eng symbol', '2 eng symbol', '15 eng symbol', '30 eng symbol', '35 eng symbol',
                              '1 spec symbol', '2 spec symbol', '15 spec symbol', '30 spec symbol', '35 spec symbol',
                              '1 num symbol', '2 num symbol', '15 num symbol', '30 num symbol', '35 num symbol'])
def test_name_registration_negativ(web_browser, name_reg):
    page = RegPage(web_browser)
    page.btn_checkin.click()
    page.wait_page_loaded()
    assert page.page_reg.get_text() == "Регистрация"
    page.first_name.send_keys(name_reg)
    page.btn_registration.click()
    page.wait_page_loaded()
    assert page.msg.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# RT-23 - Ввод имени, вводимого при регистрации, соответствующее требованиям
@pytest.mark.parametrize('name_reg', [generate_rus_string(2), generate_rus_string(15), generate_rus_string(30)],
                         ids=['2 rus symbol', '15 rus symbol', '30 rus symbol'])
def test_name_registration_positiv(web_browser, name_reg):
    page = RegPage(web_browser)
    page.btn_checkin.click()
    page.wait_page_loaded()
    assert page.page_reg.get_text() == "Регистрация"
    page.first_name.send_keys(name_reg)
    page.btn_registration.click()
    page.wait_page_loaded()
    assert page.msg.is_presented() is False
