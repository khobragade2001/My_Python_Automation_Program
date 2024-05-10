from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
x = By.XPATH
select_window = driver.window_handles

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(x, "//a[normalize-space()='Click Here']").click()
### ---------------------------- GET TEXT FROM WEBSIDE -----------------------------------------------------
text1 = driver.find_element(x,"//div[@class='example']").text
text2 = driver.find_element(x,"//div[@class='large-4 large-centered columns']//div[1]").text

print(text2)
print(text1)
time.sleep(2)

driver.switch_to.window(select_window[0])
time.sleep(5)
