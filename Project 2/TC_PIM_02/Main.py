#Test case PIM 02 => Validating options availabel in Admin page
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
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
            #Input username, password and logging in.
            self.driver.find_element(by=By.NAME, value=locators.WebApp_Locators().username_input_box).send_keys(data.WebApp_Data().username)
            self.driver.find_element(by=By.NAME, value=locators.WebApp_Locators().password_input_box).send_keys(data.WebApp_Data().password)
            self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().submit_button).click()

        #Exception handling
        except NoSuchElementException as selenium_error:
            print(selenium_error)

    def AdminOptions(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            self.driver.find_element(By.XPATH, locators.WebApp_Locators().admin_button).click()

            #Validating title of the webpage
            Title = data.WebApp_Data().title_name
            if Title in self.driver.title:
                print(Title, "is the title of the current webpage and is verified")
            else:
                print(Title, "is not the title of the curent webpage")

            #validating the options displayed in Admin page
            options_path = locators.WebApp_Locators().option_tab
            options_path1 = locators.WebApp_Locators().option_tab1
            Options_input = data.WebApp_Data().opt
            Options_output=[]
            for i in options_path:
                var = wait.until(EC.visibility_of_element_located((By.XPATH, i))).text
                Options_output.append(var)
            for j in options_path1:
                var1 = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, j))).text
                Options_output.append(var1)
            Options_output.sort()
            Options_input.sort()
            #comparing the options which are availabe or not with given input
            assert Options_input == Options_output, f"{(set(Options_input).difference(Options_output))} option is not available"
            print("All the given options are displayed in Admin page")
            
        #Exception handling
        except TimeoutException:
            print("Timeout Error")
        except NoSuchElementException as selenium_error:
            print(selenium_error)
        finally:
            #closing browser
            self.driver.close()
#creating object for the class and calling the function using object
Obj=Project()
Obj.Login()
Obj.AdminOptions()