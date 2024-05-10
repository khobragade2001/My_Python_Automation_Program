import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


opt = webdriver.ChromeOptions()
opt.add_argument("headless")
d = webdriver.Chrome(options=opt)
x = By.XPATH


d.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)
d.find_element(x, "//button[@onclick='jsAlert()']").click()
time.sleep(3)

############# Alert ##############
Alert(d).accept()
print(d.find_element(x, "//p[@id='result']").text)
# to copy Alert successfull massage

#################### conform Alert  ####################
d.find_element(x, "//button[@onclick='jsConfirm()']").click()
time.sleep(2)
Alert(d).accept()
time.sleep(2)
print(d.find_element(x, "//p[@id='result']").text)

