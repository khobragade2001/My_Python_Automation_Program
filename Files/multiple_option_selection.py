import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.maximise_window()
d.implicitly_wait(10)
x = By.XPATH
a = ActionChains(d)

d.get("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\ashish.html")
d.find_element(x, "//li[normalize-space()='1']").click()
time.sleep(2)
one = d.find_element_by_name('one')
four = d.find_element_by_name('four')
three = d.find_element_by_name('three')

a.key_down(keys.Keys.CONTROL)
# a.click(one)
time.sleep(1)
a.click(four)
time.sleep(3)
a.click(three)
a.perform()
time.sleep(1)
d.save_screenshot("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\multiple_selection022.png")

