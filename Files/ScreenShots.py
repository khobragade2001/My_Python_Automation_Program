import time
from selenium import webdriver
from selenium.webdriver.common.by import By

### headless mode
opt = webdriver.ChromeOptions()
opt.add_argument("headless")
driver = webdriver.Chrome(options=opt)
# driver = webdriver.Chrome()
x = By.XPATH

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximise_window()
driver.find_element(x, "//input[@id='checkBoxOption2']").click()
driver.save_screenshot("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\screenshots_headless.png")
time.sleep(2)