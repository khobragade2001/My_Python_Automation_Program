from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
x = By.XPATH
d.implicitly_wait(15)
d.get("https://fast.com/")





