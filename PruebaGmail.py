import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

    def test_buscar_xpath(self):
        driver = self.driver
        driver.get("http://www.gmail.com")    
        time.sleep(3)
        buscar_por_xpath = driver.find_element_by_xpath("//*[@id='identifierId']")
        time.sleep(3)
        buscar_por_xpath.send_keys("francisconava125@gmail.com")
        buscar_por_xpath.send_keys(Keys.ENTER)

        buscar_por_xpath = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
        time.sleep(3)
        buscar_por_xpath.send_keys("francisconava125@gmail.com")
        buscar_por_xpath.send_keys(Keys.ENTER)
        time.spleep(3)
        

    def tearDown(self) :
        self.driver.close()       

if __name__ == "__main__":
    unittest.main()     

    
