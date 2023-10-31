from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
 
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


usernameText = driver.find_element(By.ID, "user-name")
usernameText.send_keys("standard_user")
time.sleep(1)

PasswordText = driver.find_element(By.ID, "password")
PasswordText.send_keys("secret_sauce")
time.sleep(1)

LoginButtom = driver.find_element(By.ID, "login-button").click()

cartButton = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(2)
cartButton = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
time.sleep(2)
cartButton = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
time.sleep(2)
cartButton = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
time.sleep(2)
cartButton = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
time.sleep(2)
cartButton = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
time.sleep(2)

shopButton = driver.find_element(By.ID, "shopping_cart_container").click()
time.sleep(2)

shopButton = driver.find_element(By.ID, "checkout").click()
time.sleep(2)

firstName = driver.find_element(By.ID, "first-name")
firstName.send_keys("Abirami")
time.sleep(1)

lastName = driver.find_element(By.ID, "last-name")
lastName.send_keys("Selvan")
time.sleep(1)

postalCode = driver.find_element(By.ID, "postal-code")
postalCode.send_keys("638 502")
time.sleep(1)

continueButton = driver.find_element(By.ID, "continue").click()
time.sleep(2)

finishButton = driver.find_element(By.ID, "finish").click()
time.sleep(2)

homeButton = driver.find_element(By.ID, "back-to-products").click()
time.sleep(2)

time.sleep(10)

driver.quit()

