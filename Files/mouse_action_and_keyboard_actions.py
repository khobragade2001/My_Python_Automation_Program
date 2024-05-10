import time
from argparse import Action
from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/hovers")
driver.maximize_window()
x = By.XPATH

action = ActionChains(driver)

one = driver.find_element(x, "//div[@class='example']//div[1]//img[1]")
three = driver.find_element(x, "//div[3]//img[1]")
action.move_to_element(one).perform()
driver.save_screenshot("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\img.jpg")

action.move_to_element(three).perform()
driver.save_screenshot("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\img002.png")
