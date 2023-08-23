import time
from termcolor import colored

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebElement(object):

    _locator = ('', '')
    _web_driver = None
    _page = None
    _timeout = 10
    _wait_after_click = 10

    def __init__(self, timeout=10, wait_after_click=False, **kwargs):
        self._timeout = timeout
        self._wait_after_click = wait_after_click

        for attr in kwargs:
            self._locator = (str(attr).replace('_', ' '), str(kwargs.get(attr)))

    def find(self, timeout=10):
        """ Находит элемент на странице """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
               EC.presence_of_element_located(self._locator)
            )
        except:
            print(colored('Element not found on the page!', 'red'))

        return element

    def wait_to_be_clickable(self, timeout=10, check_visibility=True):
        """ Ждёт пока элемент не станет кликабельным """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.element_to_be_clickable(self._locator)
            )
        except:
            print(colored('Element not clickable!', 'red'))

        if check_visibility:
            self.wait_until_not_visible()

        return element

    def is_clickable(self):
        """ Проверяет, кликабелен ли элемент """

        element = self.wait_to_be_clickable(timeout=0.1)
        return element is not None

    def is_presented(self):
        """ Проверяет, есть ли элемент на странице """

        element = self.find(timeout=0.1)
        return element is not None

    def is_visible(self):
        """ Проверяет, виден ли элемент """

        element = self.find(timeout=0.1)

        if element:
            return element.is_displayed()

        return False

    def wait_until_not_visible(self, timeout=10):

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.visibility_of_element_located(self._locator)
            )
        except:
            print(colored('Element not visible!', 'red'))

        if element:
            js = ('return (!(arguments[0].offsetParent === null) && '
                  '!(window.getComputedStyle(arguments[0]) === "none") &&'
                  'arguments[0].offsetWidth > 0 && arguments[0].offsetHeight > 0'
                  ');')
            visibility = self._web_driver.execute_script(js, element)
            iteration = 0

            while not visibility and iteration < 10:
                time.sleep(0.5)

                iteration += 1

                visibility = self._web_driver.execute_script(js, element)
                print('Element {0} visibility: {1}'.format(self._locator, visibility))

        return element

    def send_keys(self, keys, wait=2):
        """ Устанавливает значение элементу """

        keys = keys.replace('\n', '\ue007')

        element = self.find()

        if element:
            element.click()
            element.clear()
            element.send_keys(keys)
            time.sleep(wait)
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def get_text(self):
        """ Получает текст элемента """

        element = self.find()
        text = ''

        try:
            text = str(element.text)
        except Exception as e:
            print('Error: {0}'.format(e))

        return text

    def get_attribute(self, attr_name):
        """ Получает атрибут элемента """

        element = self.find()

        if element:
            return element.get_attribute(attr_name)

    def _set_value(self, value, clear=True):
        """ Установка значения для входного элемента """

        element = self.find()

        if clear:
            element.clear()

        element.send_keys(value)

    def click(self, hold_seconds=0, x_offset=1, y_offset=1):
        """ Ждёт и кликает элемент """

        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset).\
                pause(hold_seconds).click(on_element=element).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

        if self._wait_after_click:
            self._page.wait_page_loaded()

    def delete(self):
        """ Удаляет элемент из страницы """

        element = self.find()

        # Delete element:
        self._web_driver.execute_script("arguments[0].remove();", element)

