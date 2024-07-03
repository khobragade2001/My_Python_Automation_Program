import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
x = By.XPATH
driver.implicitly_wait(15)
alert = Alert(driver)
driver.get("https://seleniumpractise.blogspot.com/")

## click on alert element
driver.find_element(x, "//button[@onclick='myFunction()']").click()
time.sleep(11)
alert.accept()

##======================= explicit wait ====================





