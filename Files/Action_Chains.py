import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
action = ActionChains(driver)
x = By.XPATH
def  mouse_hover():

    driver.get("https://the-internet.herokuapp.com/hovers")
    time.sleep(5)
    one = driver.find_element(x, "//div[@class='example']//div[1]//img[1]")
    three = driver.find_element(x, "//div[3]//img[1]")
    action.move_to_element(one).perform()
    action.move_to_element(three).perform()

## ENTER KEYS
def enter_keys():
    driver.get("https://the-internet.herokuapp.com/key_presses?")
    action.send_keys(Keys.ENTER).perform()
    time.sleep(2)

    ##SPACE KEYS
    action.send_keys(Keys.F1).perform()
    time.sleep(2)

def page_up():
    driver.get("https://www.britannica.com/topic/list-of-countries-1993160")
    action.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)
    action.send_keys(Keys.END).perform()       ##at the bottom of the page
    time.sleep(2)
    action.send_keys(Keys.HOME).perform()       ### return at top of the page
    time.sleep(2)


def slider_perform():
    driver.get("https://www.snapdeal.com/products/electronics-bluetooth-speakers?sort=plrty")
    slider1= driver.find_element(x, "//a[contains(@class, 'left-handle')]")
    slider2 = driver.find_element(x, "//a[contains(@class, 'right-handle')]")
    action.drag_and_drop_by_offset(slider1,50,0).perform()
    time.sleep(2)
    ## reverse direction slider
    action.click_and_hold(slider2).pause(1).move_by_offset(-60,0).release().perform()       ## you can  also used this method to perfom slider
    time.sleep(2)

def drag_and_drop_perform():
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    drag = driver.find_element(x, "//div[@id='column-a']")
    drop = drag.find_element(x ,"//div[@id='column-b']")
    action.drag_and_drop(drag,drop).perform()
    time.sleep(3)

    ## anather method
    action.drag_and_drop_by_offset(drag,234,  0).perform()
    time.sleep(5)




## calling of functions
mouse_hover()
enter_keys()
page_up()
slider_perform()
drag_and_drop_perform()