# Disclaimer!
# This is ONLY for teaching purposes.
# We decline ALL the responsability for an improper usage

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.booking.com/")

element_input = driver.find_elements_by_class_name("sb-searchbox__input")[0]
element_input.send_keys('Milan')
time.sleep(2)
element_input.send_keys(Keys.ENTER)

time.sleep(2)
boxes = driver.find_elements_by_class_name('sr-hotel__name')

names = list()
for box in boxes:
    names.append(box.text)

with open('hotel_names.txt', 'w') as F:
    F.write("\n".join(names))

driver.close()
