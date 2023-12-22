#Test case PIM 03 => Main Menu validation on Admin Page
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
            #validating the Menu options in Admin page
            Menu_items = data.WebApp_Data().Menu_bars
            Options_path = locators.WebApp_Locators().option_tab
            Options_output = []
            for i in Options_path:
                var = wait.until(EC.visibility_of_element_located((By.XPATH, i))).text
                Options_output.append(var)

            assert Options_output == Menu_items, f"{(set(Menu_items).difference(Options_output))} menu is not available"
            print("All the given Menus are available")

        #Exception handling
        except NoSuchElementException as selenium_error:
            print(selenium_error)
        finally:
            #closing browser
            sleep(2)
            self.driver.close()
#creating object for the class and calling the function using object
Obj=Project()
Obj.Login()
Obj.AdminOptions()