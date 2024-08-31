import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the desired webpage
driver.get("https://the-internet.herokuapp.com/forgot_password")

# Locate the reference element using XPath
reference_element = driver.find_element(By.XPATH, "//i[@class='icon-2x icon-signin']")

# Use locate_with to find the input element above the reference element
driver.find_element(locate_with(By.TAG_NAME, "input").above(reference_element)).send_keys("boss")

## others method
# element = driver.find_element(locate_with(By.TAG_NAME, "input").below(reference_element))
# element = driver.find_element(locate_with(By.TAG_NAME, "input").to_left_of(reference_element))
# element = driver.find_element(locate_with(By.TAG_NAME, "input").to_right_of(reference_element))



# Pause execution for 5 seconds
time.sleep(5)

# Quit the driver
driver.quit()
