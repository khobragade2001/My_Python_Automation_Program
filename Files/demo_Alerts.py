# Alerts are a way to show popups in the browser for either accepting data or displaying data.
# Selenium provides methods to handle alerts of all kinds.
# class selenium.webdriver.common.alert.Alert(driver) handles all alerts in Selenium Python.
# It contains methods for dismissing, accepting, inputting, and getting text from alert prompts.
# The two major tasks in alerts are accepting an alert or dismissing a alert.
# Selenium provides two methods for the same –
# Alert(driver).accept()
# Alert(driver).dismiss()

import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
x = By.XPATH
# create alert object
alert = Alert(d)


d.maximize_window()
d.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)
d.find_element(x, "//button[@onclick='jsAlert()']").click()
time.sleep(3)


############################## Alert ###############################
alert.accept()
print(d.find_element(x, "//p[@id='result']").text)
# to copy Alert successfull massage

#################### conform Alert  ####################
d.find_element(x, "//button[@onclick='jsConfirm()']").click()
time.sleep(2)
#####@@@@@@@@@@@@@@  Alert method  @@@@@@@@@@@@@@@
alert.dismiss()
alert.accept()
alert.send_keys()
print(alert.text)
time.sleep(2)
print(d.find_element(x, "//p[@id='result']").text)

##################### Prompt Alert ############################
d.find_element(x, "//button[@onclick='jsPrompt()']").click()
time.sleep(2)
alert.send_keys("BOSS")
alert.accept()
time.sleep(2)
print(d.find_element(x, "//p[@id='result']").text)
