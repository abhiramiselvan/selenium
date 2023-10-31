from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")


firstname = driver.find_element(By.NAME, "firstname")
firstname.send_keys("Abirami")

lastName = driver.find_element(By.NAME, "lastname")
lastName.send_keys("Selvan")
time.sleep(1)

genderradio = driver.find_element(By.ID, "sex-1").click()
time.sleep(1)

expradio = driver.find_element(By.ID, "exp-2").click()
time.sleep(1)

date = driver.find_element(By.ID, "datepicker")
date.send_keys("01-11-2023")
time.sleep(1)

profcheckbox = driver.find_element(By.ID, "profession-1").click()
time.sleep(1)

toolcheckbox = driver.find_element(By.ID, "tool-2").click()
time.sleep(1)

continentslist = Select(driver.find_element(By.ID, "continents"))
continentslist.select_by_visible_text("Europe")
time.sleep(1)

sellist = Select(driver.find_element(By.ID, "selenium_commands"))
sellist.select_by_visible_text("Wait Commands")
time.sleep(1)

file_input = driver.find_element(By.ID, "photo")
file_input.send_keys("C:\\Users\\user\\OneDrive\\Documents\\01-Software\\sel")



time.sleep(1)

endButton = driver.find_element(By.ID, "submit").click()
time.sleep(2)

driver.quit()