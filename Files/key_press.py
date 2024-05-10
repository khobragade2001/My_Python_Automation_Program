#####ActionChains are a way to automate low-level interactions such as mouse movements,
# mouse button actions, keypress, and context menu interactions.
# This is useful for doing more complex actions like hover over and drag and drop.
# Action chain methods are used by advanced scripts where we need to drag an element, click an element,
# This article revolves around how to manipulate DOM using Action Chains in Selenium.
# We have covered all the methods with examples int detail. ActionChains are
# implemented with the help of a action chain object which stores the actions in a queue and when perform() is called,
# performs the queued operations.
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.maximise_window()
d.implicitly_wait(10)
x = By.XPATH

d.get("https://the-internet.herokuapp.com/key_presses")
a = ActionChains(d)
a.send_keys(keys.Keys.ENTER).perform()
time.sleep(3)
d.save_screenshot("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\keys.png")
#
## entering down arrow keys
a.send_keys(keys.Keys.ARROW_DOWN).perform()
d.save_screenshot("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\keys_dow_narrow.png")

# ## right click
r = d.find_element(x, "//input[@id='target']")
a.context_click(r).perform()
d.save_screenshot("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\screenshots\\right_click1.png")


