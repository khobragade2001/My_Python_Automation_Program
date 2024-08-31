from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def multiple_time_run():
    x = By.XPATH
    opt = Options()
    opt.add_argument("--incognito")
    driver = webdriver.Chrome(options=opt)
    driver.maximize_window()
    driver.get("https://seleniumpractise.blogspot.com/")
    driver.find_element(x, "//input[@id='user']").send_keys("khobragade2001")
    driver.find_element(x, "//input[@id='pass1']").send_keys("654321")
    driver.find_element(x, "//button[@type='submit']").click()
    driver.quit()

n = int(input("Enter how many times webside you want to Run :"))
for i in range(n):
    multiple_time_run()