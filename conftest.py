import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def web_browser():
   driver = webdriver.Chrome()
   driver.get("https://b2c.passport.rt.ru")
   driver.set_window_size(1500, 800)

   yield driver

   driver.quit()




