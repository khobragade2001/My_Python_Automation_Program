import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
x = By.XPATH

driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
# time.sleep(3)
driver.find_element(x, "//input[@id='datepicker']").click()
a = driver.find_elements(x, "//table[@class='ui-datepicker-calendar']//a")
print(a)
for i in a:
    s = i.text
    print(s)
    if s == "31":
        i.click()
        break
driver.save_screenshot("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\date.png")

time.sleep(2)





# driver.save_screenshot("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\dates.png")