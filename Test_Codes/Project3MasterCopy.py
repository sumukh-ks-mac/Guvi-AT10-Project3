from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import data
import pytest
import time


class Test_Sumukh:
    url = "https://opensource-demo.orangehrmlive.com"
    
    # Booting Method for running the Python Tests
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()

    #TC_PIM_01 : Search - Text Box Validation on Admin Page.

    def test_TC_Login_01(self, booting_function):
        print("Test Objective : Search - (Text Box) Validation on the Admin Page")
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Login is successful")
        print("Validating the different menu options present on the side pane.")
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a") #Admin
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.PIM_xpath) #PIM
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a") #Leave
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a") #Time
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a") #Recruitment
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a") #My Info
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a") #Performance
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a") #Dashboard
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a") #Directory
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a") #Maintenance
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a") #Buzz
        print("Asserting Text Box")
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input")
        print("Text Box is present")
        print("Clicking on the text box and searching for various menu options")
        print("Validating Admin")
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("Admin")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").text == "Admin" #Admin
        print("Admin is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("admin")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").text == "Admin" #Admin
        print("admin is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.

        print("Validating PIM")
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("PIM")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "PIM" #PIM
        print("PIM is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("pim")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "PIM" #pim
        print("pim is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.

        print("Validating Leave")
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("Leave")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Leave" #Leave
        print("Leave is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("leave")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Leave" #leave
        print("leave is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.


        print("Validating Time")
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("Time")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Time" #Time
        print("Time is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("time")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Time" #time
        print("time is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.


        print("Validating Recruitment")
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("Recruitment")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Recruitment" #Recruitment
        print("Recruitment is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("recruitment")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Recruitment" #Recruitment
        print("recruitment is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.



        print("Validating My Info")
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("My Info")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "My Info" #My Info
        print("My Info is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("my info")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "My Info" #My Info
        print("my info is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.



        print("Validating Performance")
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("Performance")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Performance" #Performance
        print("Performance is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("performance")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Performance" #Performance
        print("performance is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.



        print("Validating Dashboard")
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("Dashboard")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Dashboard" #Dashboard
        print("Dashboard is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("dashboard")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Dashboard" #Dashboard
        print("dashboard is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.



        print("Validating Directory")
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("Directory")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Directory" #Directory
        print("Directory is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("directory")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Directory" #Directory
        print("directory is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.



        print("Validating Maintenance")
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("Maintenance")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Maintenance" #Maintenance
        print("Maintenance is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("Maintenance")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Maintenance" #Maintenance
        print("maintenance is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.



        print("Validating Buzz")
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("Buzz")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Buzz" #Buzz
        print("Buzz is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("buzz")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").text == "Buzz" #Buzz
        print("buzz is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.




    #TC_PIM_02 : Validation of Page Headers - Drop Down on Admin Page
    def test_TC_Login_02(self, booting_function):
        print("Test Objective : Validation of Page Headers - Drop Down on Admin Page")
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Login is successful")
        print("Validating the different menu options present on the side pane.")
        assert self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a") #Admin
        print("Click on Admin Menu option")
        self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() 
        time.sleep(5)
        print("Clicking on User Management Dropdown")
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()
        time.sleep(1) #User Management XPATH
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a") #Value of Users
        print("Clicking on Users option from the dropdown.")
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a").click()
        time.sleep(5)
        print("Clicking on User Role dropdown Menu")
        self.driver.find_element(by=By.XPATH,  value = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]").click()
        time.sleep(1)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]").text == "Admin"
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]").text == "ESS"
        print("Admin and ESS are present within the dropdowns")
        print("Clicking on the Status Dropdown Menu")
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[1]/div[2]/i").click()
        time.sleep(1)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]").text == "Enabled"
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[3]").text == "Disabled"
        print("Enabled and Disabled are present within the dropdowns")

    #TC_PIM_03 : Creation of New Employee under PIM
    def test_TC_Login_03(self, booting_function):
        print("Test Objective : Creation of New Employee under PIM")
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Login is successful")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.PIM_xpath).click()
        print("Click on PIM was successful")
        time.sleep(data.Sumukh_Data.mediumWait )
        self.driver.find_element(by=By.LINK_TEXT, value=data.Sumukh_Selectors.tab_add_employee).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Click on Add Employee was successful")
        #Clicking on the Create Login  toggle option
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span").click() #Toggle Button
        print("Click on Toggle was successful")
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_firstname).send_keys(data.Sumukh_Data.firstName) #Fill First Name
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_lastname).send_keys(data.Sumukh_Data.lastName) #Fill Last Name
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("game1243") #Username
        self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys("Guvi@2023") #Password
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys("Guvi@2023") #Confirm Password
        #Clicking on ENabled Button
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label").click() #Enabled Radio Button
        #get info of the Employee ID
        EMP_ID = self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").text
        print("EMP ID = ", EMP_ID)
        #Click on Save
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(data.Sumukh_Data.longWait)
        print("Click on Save was successful")
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text == "Personal Details"
        print("SUCCESS # A New Employee is added into the PIM Module")
        time.sleep(data.Sumukh_Data.mediumWait)

    #TC_PIM_04 : Validation of Employee Personal details Page post user creation.
    def test_TC_Login_04(self, booting_function):
        print("Test Objective : Validation of Employee Personal details Page post user creation.")
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Login is successful")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.PIM_xpath).click()
        print("Click on PIM was successful")
        time.sleep(data.Sumukh_Data.mediumWait)
        #Enter First Name and click on Search
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstName_xpath).send_keys(data.Sumukh_Data.firstName)
        time.sleep(data.Sumukh_Data.smallWait)
        print("Click on Search")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.search_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on the first row check box
        print("Click on the first checkbox")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstCheckBox_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on Edit icon
        print("Click on the Edit Icon")
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]").click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a").text == "Personal Details"
        print("Personal Details is present")
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a").text == "Contact Details"        
        print("Contact Details is present")
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]").text == "Emergency Contacts"        
        print("Emergency Contacts is present")
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]").text == "Dependents"        
        print("Dependents is present")
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]").text == "Immigration"        
        print("Immigration is present")
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]").text == "Job"        
        print("Job is present")
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]").text == "Salary"        
        print("Salary is present")
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]").text == "Tax Exemptions"        
        print("Tax Exemptions is present")
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]").text == "Report-to"        
        print("Report-to is present")
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]").text == "Qualifications"        
        print("Qualifications is present")
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[11]").text == "Memberships"        
        print("Memberships is present")

    #TC_PIM_05 : Updating Employee Personal details Page post user creation.
    def test_TC_Login_05(self, booting_function):
        print("Test Objective : Updating Employee Personal details Page post user creation.")
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Login is successful")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.PIM_xpath).click()
        print("Click on PIM was successful")
        time.sleep(data.Sumukh_Data.mediumWait)
        #Enter First Name and click on Search
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstName_xpath).send_keys(data.Sumukh_Data.firstName)
        time.sleep(data.Sumukh_Data.smallWait)
        print("Click on Search")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.search_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on the first row check box
        print("Click on the first checkbox")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstCheckBox_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on Delete icon
        print("Click on the Edit Icon")
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]").click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        #Click on Male Radio Button 
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label").click()#Gender
        time.sleep(1)
        #Select Nationality
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]").click()#Click on Nationality dropdown
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[83]").click()#Nationality - Indian
        time.sleep(1)
        #Select Date of Birth
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input").send_keys("1995-04-25")#Date Picker
        time.sleep(1)
        #Enter SSN
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input").send_keys("878777")#SSN
        time.sleep(1)
        #Enter Marital Status
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]").click()#Click on the dropdown of marital status
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]").click()#Select Single
        time.sleep(1)
        #Save all Personal Details
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click() #First Save
        time.sleep(10)
        assert self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input").get_attribute('value') == "878777" #SSN
        assert self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]").text == "Indian" #Nationality
        assert self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]").text == "Single" #Marital Status
        assert self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input").get_attribute('value') == "1995-04-25" #DOB
        
    
    #TC_PIM_06 : Updating Employee Contact details Page post user creation.
    def test_TC_Login_06(self, booting_function):
        print("Test Objective : Updating Employee Contact details Page post user creation.")
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Login is successful")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.PIM_xpath).click()
        print("Click on PIM was successful")
        time.sleep(data.Sumukh_Data.mediumWait)
        #Enter First Name and click on Search
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstName_xpath).send_keys(data.Sumukh_Data.firstName)
        time.sleep(data.Sumukh_Data.smallWait)
        print("Click on Search")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.search_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on the first row check box
        print("Click on the first checkbox")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstCheckBox_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on Delete icon
        print("Click on the Edit Icon")
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]").click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a").click()
        time.sleep(3)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text == "Contact Details"
        print("SUCCESS # Contact details is opened for the employee")
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Bangalore") #Street1
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Karnataka") #State
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div").click()#Click on Country dropdown
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[100]").click()#Country - India
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input").send_keys("123456789")#Home Number
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input").send_keys("project@AT.com")#Email
        time.sleep(1)
        #Click on Save
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button").click()
        time.sleep(5)
        assert self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").get_attribute('value') == "Bangalore" #Street1
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input").get_attribute('value') == "Karnataka" #State
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div").text == "India" #Country
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input").get_attribute('value') == "123456789" #Home Number
        assert self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input").get_attribute('value') == "project@AT.com"#Email
        print("All field Asserted Successfully")

    #TC_PIM_07 : Updating Employee Contact details Page post user creation.
    def test_TC_Login_07(self, booting_function):
        print("Test Objective : Updating Employee Contact details Page post user creation.")
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Login is successful")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.PIM_xpath).click()
        print("Click on PIM was successful")
        time.sleep(data.Sumukh_Data.mediumWait)
        #Enter First Name and click on Search
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstName_xpath).send_keys(data.Sumukh_Data.firstName)
        time.sleep(data.Sumukh_Data.smallWait)
        print("Click on Search")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.search_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on the first row check box
        print("Click on the first checkbox")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstCheckBox_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on Delete icon
        print("Click on the Edit Icon")
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]").click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a").click()
        time.sleep(6)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/h6").text == "Assigned Emergency Contacts"
        print("SUCCESS # Emergency Contact details is opened for the employee")
        #Clicking on Add button
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click()
        time.sleep(5)
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text == "Save Emergency Contact"
        #Enter Name
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Scale")
        time.sleep(1)
        #Enter Relationship
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("Friend")
        time.sleep(1)
        #Enter Mobile Number
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input").send_keys("123456789")
        time.sleep(2)
        #Click on Save
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]").click()
        time.sleep(6)
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div").text == "Scale"
        print("Name is successfully asserted")
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div[3]/div").text == "Friend"
        print("Relationship is successfully asserted")
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div[5]/div").text == "123456789"
        print("Mobile is successfully asserted")

    #TC_PIM_08 : Updating Employee Contact details Page post user creation.
    def test_TC_Login_08(self, booting_function):
        print("Test Objective : Updating Employee Contact details Page post user creation.")
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Login is successful")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.PIM_xpath).click()
        print("Click on PIM was successful")
        time.sleep(data.Sumukh_Data.mediumWait)
        #Enter First Name and click on Search
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstName_xpath).send_keys(data.Sumukh_Data.firstName)
        time.sleep(data.Sumukh_Data.smallWait)
        print("Click on Search")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.search_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on the first row check box
        print("Click on the first checkbox")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstCheckBox_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on Delete icon
        print("Click on the Edit Icon")
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]").click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a").click()
        time.sleep(6)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/h6").text == "Assigned Dependents"
        print("SUCCESS # Emergency Contact details is opened for the employee")
        #Clicking on Add button
        self.driver.find_element(by=By.XPATH, value = "//html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Jack") #Name of Dependent
        time.sleep(1)
        #Select Relationship
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[1]/div[1]").click() #Click on the dropdown
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]").click() #Select Child.
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div/input").send_keys("2000-12-12")#DOB
        time.sleep(2)
        #Clicking on Save
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]").click()#Click on Save
        time.sleep(6)
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div").text == "Jack"
        print("Name is successfully asserted")
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").text == "Child"
        print("Relationship is successfully asserted")
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div").text == "2000-12-12"
        print("DOB is successfully asserted")        

    #TC_PIM_09 : Updating Employee Contact details Page post user creation.
    def test_TC_Login_09(self, booting_function):
        print("Test Objective : Updating Employee Contact details Page post user creation.")
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Login is successful")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.PIM_xpath).click()
        print("Click on PIM was successful")
        time.sleep(data.Sumukh_Data.mediumWait)
        #Enter First Name and click on Search
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstName_xpath).send_keys(data.Sumukh_Data.firstName)
        time.sleep(data.Sumukh_Data.smallWait)
        print("Click on Search")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.search_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on the first row check box
        print("Click on the first checkbox")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstCheckBox_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on Delete icon
        print("Click on the Edit Icon")
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]").click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a").click()
        time.sleep(6)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text == "Job Details"
        print("SUCCESS # Emergency Contact details is opened for the employee")
        #Enter Joining Date
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("2020-01-01") #Enter Joinging Date
        time.sleep(1)
        #Select Job Title
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]").click()
        time.sleep(1)
        #select from dropdown
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]").click()#Selected Dropdown value
        time.sleep(1)
        #select Job Category
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div").click() #Select Job Category
        time.sleep(1)
        #Select from Dropdown
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]").click() #Craft Workers
        time.sleep(1)
        #select Sub Unit
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[1]").click() #sub unit
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div[2]/div[2]").click() #selected Administration
        time.sleep(1)
        #Select Location
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]").click()
        time.sleep(1)
        #select from location dropdown
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[2]").click() #Canadian Regional HQ
        time.sleep(1)
        #select Employment Status
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[1]").click() #EMP STatus
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div[2]/div[2]").click() #Freelance
        time.sleep(1)
        #clicking on the toggle of Include Employment Contract Details
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/label/span").click()
        time.sleep(2)
        #Enter Contract Start Date
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input").send_keys("2020-01-01")
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input").send_keys("2021-01-01")
        time.sleep(2)
        #click on Save
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click()
        time.sleep(8)
        print("Asserting all values")
        assert self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input").get_attribute('value') == "2020-01-01" #joining date
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]").text == "Account Assistant"
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div").text == "Craft Workers"
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[1]").text == "Administration"
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]").text == "Canadian Regional HQ"
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[1]").text == "Freelance"
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input").get_attribute('value') == "2020-01-01"
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input").get_attribute('value') == "2021-01-01"
        print("All Values Asserted Successfully")

    #TC_PIM_10 : Updating Employee Contact details Page post user creation.
    def test_TC_Login_10(self, booting_function):
        print("Test Objective : Updating Employee Contact details Page post user creation.")
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Login is successful")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.PIM_xpath).click()
        print("Click on PIM was successful")
        time.sleep(data.Sumukh_Data.mediumWait)
        #Enter First Name and click on Search
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstName_xpath).send_keys(data.Sumukh_Data.firstName)
        time.sleep(data.Sumukh_Data.smallWait)
        print("Click on Search")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.search_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on the first row check box
        print("Click on the first checkbox")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstCheckBox_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on Delete icon
        print("Click on the Edit Icon")
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]").click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a").click()
        time.sleep(6)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text == "Job Details"
        print("SUCCESS # Emergency Contact details is opened for the employee")
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button").click() #Click on Terminate Employment
        time.sleep(5)
        #assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div/p").text == "Terminate Employment"
        print("Terminate Employment window is opened.") 
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input").send_keys("2021-01-01")
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div/div[1]").click() #Clicking on Terminate Reason Dropdown
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div[2]/div[2]").click() #Clicking on the options
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[4]/button[2]").click() #Click on Save
        time.sleep(8)
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/p").text == "Terminated on: 2021-01-01"   
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button")
        print("Employee Terminated Successfully")
        #Continuing to execute TC_PIM_11 Test Case inside this block since Activation of the Emplpoyee is required.
        print("Executing TC_PIM_11 in this test case")
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button").click() #Activating the Employee
        time.sleep(10)
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button") #Terminate Employement is present which means the Employee is activated.

    #TC_PIM_12 : Updating Employee Contact details Page post user creation.
    def test_TC_Login_12(self, booting_function):
        print("Test Objective : Updating Employee Contact details Page post user creation.")
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Login is successful")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.PIM_xpath).click()
        print("Click on PIM was successful")
        time.sleep(data.Sumukh_Data.mediumWait)
        #Enter First Name and click on Search
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstName_xpath).send_keys(data.Sumukh_Data.firstName)
        time.sleep(data.Sumukh_Data.smallWait)
        print("Click on Search")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.search_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on the first row check box
        print("Click on the first checkbox")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstCheckBox_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on Delete icon
        print("Click on the Edit Icon")
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]").click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a").click()
        time.sleep(8)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/h6").text == "Assigned Salary Components"
        print("SUCCESS # Emergency Contact details is opened for the employee")
        #click on Add
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("AGC")
        time.sleep(1)
        #self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]").click() #Pay Grade Dropdown
        time.sleep(2)
        #self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/span").click() #Grade 1
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]").click() #Pay Frequency Dropdown
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[4]").click() #Monthly
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div").click() #Currency Drop Down
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]").click() #USD
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input").send_keys("55000") #Amount
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/label/span").click() #Direct Deposit Toggle Button
        time.sleep(3)
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[1]/label") #Account Number
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[1]/label") #Account Type
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[1]/label") #Routing Number
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[1]/label") #Amount
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input").send_keys("9999999999") #Account Number
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]").click() #Savings
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input").send_keys("1234") #Rounting Number
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input").send_keys("55000")#Amount
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button[2]").click()#Save
        time.sleep(8)
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div").text == "AGC" #Salary Component
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").text == "55000" #Amount
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div").text == "Afghanistan Afghani" #Currency
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div").text == "Monthly" #Frequency
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[6]/div").text == "55000.00" #Direct Amount
        
    #TC_PIM_13 : Updating Employee Contact details Page post user creation.
    def test_TC_Login_13(self, booting_function):
        print("Test Objective : Updating Employee Contact details Page post user creation.")
        self.driver.maximize_window()#Maximising the browser window
        time.sleep(data.Sumukh_Data.smallWait) #Wait time for Maximising Screen
        self.driver.get(self.url)
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_username).send_keys(data.Sumukh_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_password).send_keys(data.Sumukh_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.login_xpath).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        print("Login is successful")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.PIM_xpath).click()
        print("Click on PIM was successful")
        time.sleep(data.Sumukh_Data.mediumWait)
        #Enter First Name and click on Search
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstName_xpath).send_keys(data.Sumukh_Data.firstName)
        time.sleep(data.Sumukh_Data.smallWait)
        print("Click on Search")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.search_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on the first row check box
        print("Click on the first checkbox")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.firstCheckBox_xpath).click()
        time.sleep(data.Sumukh_Data.smallWait)
        #Click on Delete icon
        print("Click on the Edit Icon")
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]").click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        self.driver.find_element(by=By.XPATH, value ="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a").click()
        time.sleep(8)
        assert self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6").text == "Tax Exemptions"
        print("SUCCESS # Emergency Contact details is opened for the employee")
        #click on Status
        self.driver.find_element(by=By.XPATH, value= "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div[1]").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/span").click() #Single
        time.sleep(1)
        #Click on State       
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div").click()
        time.sleep(1)

        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]").click() #Albama
        time.sleep(1)

        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/div[1]").click()
        time.sleep(1)

        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]").click() #Single
        time.sleep(1)
        #Unemployment Status
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]").click()
        time.sleep(1)

        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]").click()#Albama
        time.sleep(1)
        #Work State
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[1]").click()
        time.sleep(1)

        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div[2]/div[2]").click() #Albama
        time.sleep(1)
        #Exemptions
        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("50")#50
        time.sleep(1)

        self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input").send_keys("50")#50
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button").click()
        print("Asserting all fields")
        time.sleep(8)
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]").text == "Single"
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/div[1]").text == "Alabama"
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/div[1]").text == "Single"
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]").text == "Alabama"
        assert self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[1]").text == "Alabama"


   