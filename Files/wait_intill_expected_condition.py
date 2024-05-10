from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

d = webdriver.Chrome()
d.maximize_window()
x = By.XPATH
d.get("https://fast.com/")
a = d.find_element(x, "//a[@id='show-more-details-link']")

wait = WebDriverWait(d, 40)
wait.until(expected_conditions.element_to_be_clickable((x, "//a[@id='show-more-details-link']"))).click()
d.save_screenshot("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\untill_exspected_condition001.png")

