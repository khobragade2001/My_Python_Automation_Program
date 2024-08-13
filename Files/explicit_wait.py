from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
x = By.XPATH
driver.get("https://fast.com/")
a = driver.find_element(x, "//a[@id='show-more-details-link']")

## wait init
wait = WebDriverWait(driver, 40)
wait.until(expected_conditions.element_to_be_clickable((x, "//a[@id='show-more-details-link']"))).click()

driver.save_screenshot("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\untill_exspected_condition008.png")

