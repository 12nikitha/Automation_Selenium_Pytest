import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from demo.utils.details import Details
class Login():
    def __init__(self,driver):
        self.driver=driver
        self.name=Details.name
        self.password=Details.password
        self.login=Details.login

    def test_enter_username(self,name):
        self.driver.find_element(By.XPATH,Details.Email ).clear()
        self.driver.find_element(By.XPATH, Details.Email).send_keys(name)

    def test_enter_password(self,code):
        self.driver.find_element(By.NAME,Details.password ).clear()
        self.driver.find_element(By.NAME, Details.password).send_keys(code)

    def test_click_login(self):
        self.driver.find_element(By.XPATH, Details.login).click()



# driver=webdriver.Chrome()
# driver.get("https://blazedemo.com/")
# driver.get("https://blazedemo.com/login")
# driver.implicitly_wait(3)
# driver.find_element(By.ID,"email").send_keys("abc2@gmail.com")
# time.sleep(2)
# driver.find_element(By.ID,"password").send_keys("abciop10")
# driver.find_element(By.XPATH,"// button[@type='submit']").click()
# time.sleep(2)
# driver.close()
# driver.quit()