import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
x = By.XPATH
driver.get("https://fast.com/")

wait = WebDriverWait(driver,15,poll_frequency=3)
wait.until(expected_conditions.element_to_be_clickable((x,"//a[@id='show-more-details-link']"))).click()
driver.save_screenshot("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\fluent_wait_001.png")
