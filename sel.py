from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import time
 
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

usernameText = driver.find_element(By.ID, "username")
usernameText.send_keys("Abirami Selvan")

PasswordText = driver.find_element(By.ID, "password")
PasswordText.send_keys("Password123")

LoginButtom = driver.find_element(By.ID, "submit").click()

time.sleep(10)

driver.quit()
