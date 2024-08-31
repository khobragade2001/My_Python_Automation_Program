from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome()
def get_cookies():
    driver.get("https://www.onlinesbi.sbi/")
    driver.maximize_window()
    
    ## add some values to cookies 
    cookies = {'name':'Ashish_cookie','value':'Khobragade2001@gmail.com'}
    driver.add_cookie(cookies)
    
    ## get all cookies
    cookie = driver.get_cookies()
    return cookie

var = get_cookies()
prity = json.dumps(var, indent=4)
print(prity)

## get specific cookies 
#spe = driver.get_cookies("value")
#print(spe)

## delete all cookie_value
driver.delete_all_cookies()
print("after delete cookie")
print(driver.get_cookies())
