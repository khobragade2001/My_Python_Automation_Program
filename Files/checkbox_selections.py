from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
x = By.XPATH
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/checkboxes")
ele1 = driver.find_element(x, "//input[1]")
time.sleep(3)

if not ele1.is_selected():
    ele1.click()
time.sleep(3)

## already selected buttom convert unselect
ele2 = driver.find_element(x, "//input[2]")
if ele2.is_selected():
    ele2.click()
time.sleep(3)

driver.quit()