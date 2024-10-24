import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium import webdriver


from demo.page.registerpage import Register
from demo.page.loginpage import Login
import HtmlTestRunner
class Registermethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome()
        cls.driver.get("https://blazedemo.com/")
        cls.driver.maximize_window()
        # yield  # in python we will use yiled -something we want to run end
        # cls.driver.close()
        # cls.driver.quit()
    def test_userdetalis(self):
        driver = self.driver

        signup = Register(self.driver)
        signup.test_homelink()
        time.sleep(3)
        signup.test_homelink2()
        signup.test_username("abcf")
        time.sleep(2)
        signup.test_company("Power")
        signup.test_mail("abc@gmail.com")
        signup.test_password("12w3")
        time.sleep(2)
        signup.test_conformpassword("12w3")
        signup.test_register()

        signin = Login(self.driver)
        driver.get("https://blazedemo.com/")
        driver.get("https://blazedemo.com/login")
        signin.test_enter_username("abc@gmail.com")
        signin.test_enter_password("12w3")
        time.sleep(2)
        signin.test_click_login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/nikitha/learn_python/selenium1/Demoseleniumpytes/demo/report"))

#
# driver.find_element(By.XPATH,"// a [@href='home']").click()
# driver.find_element(By.XPATH,"// a[@href='https://blazedemo.com/register']").click()
# driver.find_element(By.ID,"name").send_keys("sony")
# driver.find_element(By.ID,"company").send_keys("abcd")
# time.sleep(3)
# driver.find_element(By.ID,"email").send_keys("abc1@gmail.com")
# driver.find_element(By.ID,"password").send_keys("abciop0")
# driver.find_element(By.ID,"password-confirm").send_keys("abciop0")
# driver.find_element(By.XPATH,"// button[@type='submit']").click()
# time.sleep(6)
# driver.close()
# driver.quit()