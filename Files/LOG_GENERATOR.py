import inspect
import logging
import time
from venv import logger

from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
x = By.XPATH


logfile = logging.FileHandler("D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\log_generate\\log_file.log")
log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s ")
logfile.setFormatter(log_format)
logger.addHandler(logfile)
logger.setLevel(logging.INFO)

logger.info("this is stating of Logging masssage")
d.get("https://parabank.parasoft.com/parabank/index.htm")
logger.info("go to the website and wait for reload the page ")
d.find_element(x, "//a[normalize-space()='Register']").click()
logger.info("click on register button")
time.sleep(1)


#
#
# log = logging
# log.basicConfig(filename="D:\\CREDENCE CLASS\\AUTOMATION\\automation_concept\\log_generate\\log_file.log",
#                 format='%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s',
#                 datefmt='%d/%m/%Y  %I:%M:%S:%p',
#                 level=log.INFO)
#
# log.info("this is stating of Logging masssage")
# d.get("https://parabank.parasoft.com/parabank/index.htm")
# log.info("go to the website and wait for reload the page ")
# d.find_element(x, "//a[normalize-space()='Register']").click()
# log.info("click on register button")
# time.sleep(1)



