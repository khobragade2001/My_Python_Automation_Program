import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
x = By. XPATH


action = ActionChains(driver)
driver.get("https://demos.jquerymobile.com/1.4.5/slider/")
time.sleep(2)
one = driver.find_element(x, "//a[@title='6']")
action.drag_and_drop_by_offset(one,60, 0).perform()

