from selenium import webdriver
driver= webdriver.Chrome()
driver.get("https://blazedemo.com/")
driver.close()
driver.quit()
