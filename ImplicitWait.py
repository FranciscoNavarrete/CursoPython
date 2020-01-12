#implicit wait es de selenium, es parecido al time, es de python, es implicit es mas preciso a tiempo
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class usando_Unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

    def test_usando_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) #cinco Segundos
        driver.get("http://www.google.com")
        #obtener la propiedad de los componentes que tiene la posibilidas de ser dinamicos al momento de estar cambiar de imagenes videos etc
        myDynamicElement = driver.find_element_by_class_name("q")

if __name__ == "__main__":
    unittest.main()    