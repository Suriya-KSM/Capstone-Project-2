#Test case PIM01 => Forgot Password link validation on login page
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from Data import data
from Locators import locators

class Project:
    def __init__(self):
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))


    def Login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(data.WebApp_Data().url)
            self.driver.implicitly_wait(20)
            #Clicking forgot password link
            wait =  WebDriverWait(self.driver, 20)
            self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().forgot_password_link).click()
            forgot_button = wait.until(EC.presence_of_element_located((By.NAME, locators.WebApp_Locators().username_input_box)))
            forgot_button.send_keys(data.WebApp_Data().username)
            sleep(2)
            self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().reset_button).click()
            #Displaying message in console
            Reset_Message = self.driver.find_element(By.XPATH, locators.WebApp_Locators().reset_message)
            print(Reset_Message.text)
            sleep(3)
        #Exception handling
        except NoSuchElementException as selenium_error:
            print(selenium_error)
        #Closing browser        
        finally:
            self.driver.close()

Obj=Project()
Obj.Login()