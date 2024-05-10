import time
from lib2to3.pgen2 import driver

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    request.cls.driver = driver
    yield
    driver.close()






