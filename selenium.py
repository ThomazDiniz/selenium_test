import os
import re
import subprocess
import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
driver.get("https://www.google.com.br/")

text_box = driver.find_element(by=By.ID, value="APjFqb")
text_box.send_keys("Selenium")

time.sleep(2)
submit_button = driver.find_element(by=By.NAME, value="btnK")
submit_button.click()

time.sleep(5)

text = driver.find_element(by=By.CLASS_NAME, value="VwiC3b")
print(text.get_attribute('innerHTML'))

time.sleep(60)
