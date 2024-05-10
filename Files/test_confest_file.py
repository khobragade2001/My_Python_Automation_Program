import time
import pytest
from selenium.webdriver.common.by import By


x = By.XPATH

@pytest.mark.usefixtures("setup")
class Testconfigure_file:

    def test_demo(self):
        self.driver.find_element(x, "//a[normalize-space()='Register']").click()
        time.sleep(2)

    def test_demo_002_file(self):
        self.driver.find_element(x, "//a[normalize-space()='Withdraw Funds']").click()
        time.sleep(2)


    def  test_deom_003_file(self):
        self.driver.find_element(x, "//a[normalize-space()='Bill Pay']").click()
        time.sleep(3)


