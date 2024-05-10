import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
x = By.XPATH

action = ActionChains(driver)
driver.get("https://www.makemytrip.com/")

var = driver.find_element(x, "//span[normalize-space()='Introducing myBiz']")
action.move_to_element(var).perform()
driver.save_screenshot("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\mouse_hover.png")
time.sleep(2)

