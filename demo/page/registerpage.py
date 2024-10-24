import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from demo.utils.details import Details

class Register():
    def __init__(self,driver):
        self.driver= driver
        self.home_link= Details.link
        self.register_link=Details.register_link
        self.name=Details.name
        self.company=Details.company
        self.email=Details.Email
        self.password=Details.password
        self.conform_password=Details.conform_password
        self.register_button=Details.button
    def test_homelink(self):
        self.driver.find_element(By.XPATH, Details.link).click()
    def test_homelink2(self):
        self.driver.find_element(By.XPATH,Details.register_link ).click()
    def test_username(self,Name):
        self.driver.find_element(By.ID,Details.name ).send_keys(Name)
    def test_company(self,comp):
        self.driver.find_element(By.ID,Details.company ).send_keys(comp)
    def test_mail(self,mail):
        self.driver.find_element(By.ID, Details.Email).send_keys(mail)
    def test_password(self,code):
        self.driver.find_element(By.ID,Details.password ).send_keys(code)
    def test_conformpassword(self,cp):
        self.driver.find_element(By.ID, Details.conform_password).send_keys(cp)
    def test_register(self):
        self.driver.find_element(By.XPATH,Details.button ).click()




# def registerpage():
#     driver.get("https://blazedemo.com/")
#     driver.maximize_window()
#     driver.implicitly_wait(5)
# def details():
#     driver.find_element(By.XPATH, ).click()
#     driver.find_element(By.XPATH, ).click()
#     driver.find_element(By.ID, ).send_keys(name)
#     driver.find_element(By.ID, ).send_keys("")
#     time.sleep(3)
#     driver.find_element(By.ID, ).send_keys("abc2@gmail.com")
#     driver.find_element(By.ID, ).send_keys("abciop10")
#     driver.find_element(By.ID, ).send_keys("abciop10")
#     driver.find_element(By.XPATH, ).click()
#     time.sleep(6)



