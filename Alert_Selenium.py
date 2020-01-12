from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("C:/Users\walte\Desktop\FranNavarrete\Python\Alert_html.html")
time.sleep(5)

alerta_simple = driver.find_element_by_xpath("/html/body/button")
alerta_simple.click()
time.sleep(3)
alerta_simple = driver.switch_to_alert()
alerta_simple.dismiss()
time.sleep(3)
driver.close()