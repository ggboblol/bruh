import random
import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
random.seed(time.localtime)

full_name = ("gg gboblol_")
first_letter = full_name[0]
space_index = full_name.find(" ")
three_letters_surname = full_name[space_index + 1:space_index + 10]
number = random.randrange (99,99999)


#Setup Selenium
path = 'C:\\Users\\chris\\Downloads\\bot\\bin\\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(path, chrome_options=chrome_options)
driver.get("https://roblox.com")
assert "Roblox" in driver.title

#Select the birthday fields.
birthdayMonth = Select(driver.find_element_by_id("MonthDropdown"))
birthdayMonth.select_by_value("Jan")
birthdayDay = Select(driver.find_element_by_id("DayDropdown"))
birthdayDay.select_by_value("01")
birthdayYear = Select(driver.find_element_by_id("YearDropdown"))
birthdayYear.select_by_value("1990")

#Write to the username field.
username_field = driver.find_element_by_id("signup-username")
username_field.clear()
username_field.send_keys(first_letter, three_letters_surname, number)

#Write to the password field.
password_field = driver.find_element_by_id("signup-password")
password_field.clear()
password_field.send_keys("AspectNetwork01AspectNetwork01")

#Click the female gender button.
gender_button = driver.find_element_by_id("FemaleButton")
gender_button.click()

time.sleep(1)

#Click the signup button.
signup_button = driver.find_element_by_id("signup-button")
signup_button.click()


try:
    WebDriverWait(driver, 30).until(lambda x: 'Home' in driver.title)
except:
    print("pass")
    pass

rbxcookie = driver.get_cookie(".ROBLOSECURITY")
print(rbxcookie["value"])
currentcookielog = open("currentcookie.log", "a")
currentcookielog.write(rbxcookie["value"])
currentcookielog.write("                                                                                                                                                                                                                                     ")

driver.quit()