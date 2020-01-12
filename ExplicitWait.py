import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class usando_Unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

    def test_Usando_explicit_wait(self):
        driver = self.driver
        driver.get("http://www.google.com")
        #la condicion es try bucle
        #driver se le asigna un elemente
        #driver es donde se carga la pagina y se hacen 10 intentos 
        #prencense_of_elemente va a esperar que sea localizado por el nombre
        try:
            element = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.NAME, "q"))
        finally:
            driver.quit()    

if __name__ == "__main__":
    unittest.main()


