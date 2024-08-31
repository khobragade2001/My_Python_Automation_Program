from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

## refresh method
driver.refresh()
print("Refresh by refresh method")
time.sleep(2)

## navigating to the current URL
driver.get(driver.current_url)
print("Refresh by navigating to the current URL")
time.sleep(2)

# Refresh the webpage using JavaScript
driver.execute_script("location.reload();")
print("Refresh by JavaScript")
time.sleep(2)
