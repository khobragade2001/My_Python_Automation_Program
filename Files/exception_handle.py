import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
x= By.XPATH
driver.get("https://parabank.parasoft.com/parabank/index.htm")

driver.find_element(x, "//input[@name='username']").send_keys(" ")
driver.find_element(x, "//input[@name='password']").send_keys(" ")
try:
    driver.find_element(x, "//input[@value='Log In']").click()
    time.sleep(1)
except:
    print("invalid user name or passwords")
    driver.save_screenshot("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\exception_handle_002.png")

else:
    driver.save_screenshot("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\exception.png")

finally:
    print("YE TO PRINT HOGA HI HOGA .....")
    driver.quit()
