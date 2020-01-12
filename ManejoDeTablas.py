from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(3)

valor = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[3]/td[2]").text
print("El valor es: ",valor)



