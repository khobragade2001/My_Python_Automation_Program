import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
x = By.XPATH
d.maximize_window()
select_window = d.window_handles

d.get("https://the-internet.herokuapp.com/windows")
d.find_element(x, "//a[normalize-space()='Click Here']").click()
time.sleep(3)
# print(d.find_element(x, "//h3[normalize-space()='New Window']").text)
time.sleep(2)
d.switch_to.window(select_window[0])
time.sleep(2)
d.find_element(x, "//a[normalize-space()='Click Here']").click()
d.switch_to.window(select_window[0])
time.sleep(2)
# print(d.find_element(x, "//h3[normalize-space()='New Window']").text)



