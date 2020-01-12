import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.w3schools.com/jsref/met_html_click.asp")

buscar = driver.find_element_by_xpath("//*[@id='main']/p[1]/a")
time.sleep(3)
buscar.click()
time.sleep(3)
buscar = driver.switch_to_alert()
buscar.dismiss()
time.sleep(3)
driver.close()