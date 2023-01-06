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
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.admin_XPATH) #Admin
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.PIM_xpath) #PIM
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.leave_XPATH) #Leave
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.time_XPATH) #Time
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.recruitment_XPATH) #Recruitment
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.myInfo_XPATH) #My Info
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.performance_XPATH) #Performance
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.dashboard_XPATH) #Dashboard
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.directory_XPATH) #Directory
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.maintenance_XPATH) #Maintenance
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.buzz_XPATH) #Buzz
        print("Asserting Text Box")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.searchtb_XPATH)
        print("Text Box is present")
        print("Clicking on the text box and searching for various menu options")
        print("Validating Admin")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("Admin")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.admin_XPATH).text == "Admin" #Admin
        print("Admin is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("admin")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.admin_XPATH).text == "Admin" #Admin
        print("admin is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.

        print("Validating PIM")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("PIM")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "PIM" #PIM
        print("PIM is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("pim")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "PIM" #pim
        print("pim is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.

        print("Validating Leave")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("Leave")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Leave" #Leave
        print("Leave is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("leave")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Leave" #leave
        print("leave is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.


        print("Validating Time")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("Time")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Time" #Time
        print("Time is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("time")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Time" #time
        print("time is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.


        print("Validating Recruitment")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("Recruitment")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Recruitment" #Recruitment
        print("Recruitment is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("recruitment")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Recruitment" #Recruitment
        print("recruitment is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.



        print("Validating My Info")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("My Info")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "My Info" #My Info
        print("My Info is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("my info")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "My Info" #My Info
        print("my info is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.



        print("Validating Performance")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("Performance")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Performance" #Performance
        print("Performance is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("performance")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Performance" #Performance
        print("performance is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.



        print("Validating Dashboard")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("Dashboard")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Dashboard" #Dashboard
        print("Dashboard is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("dashboard")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Dashboard" #Dashboard
        print("dashboard is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.



        print("Validating Directory")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("Directory")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Directory" #Directory
        print("Directory is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("directory")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Directory" #Directory
        print("directory is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.



        print("Validating Maintenance")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("Maintenance")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Maintenance" #Maintenance
        print("Maintenance is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("Maintenance")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Maintenance" #Maintenance
        print("maintenance is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.



        print("Validating Buzz")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("Buzz")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Buzz" #Buzz
        print("Buzz is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.
        time.sleep(1)#Asserting with lowercase of admin.
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.searchtb_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys("buzz")
        time.sleep(1)        
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.serOpt_XPATH).text == "Buzz" #Buzz
        print("buzz is present")
        time.sleep(1)        
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.COMMAND, 'a') #Using COMMAND because i am using a Mac. 
        time.sleep(1)       
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.searchtb_XPATH).send_keys(Keys.BACKSPACE) #Clearing the text on the textbox.




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
        assert self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.admin_XPATH) #Admin
        print("Click on Admin Menu option")
        self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.admin_XPATH).click() 
        time.sleep(5)
        print("Clicking on User Management Dropdown")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.userMang_XPATH).click()
        time.sleep(1) #User Management XPATH
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.usersVal_XPATH) #Value of Users
        print("Clicking on Users option from the dropdown.")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.usersVal_XPATH).click()
        time.sleep(5)
        print("Clicking on User Role dropdown Menu")
        self.driver.find_element(by=By.XPATH,  value = data.Sumukh_Selectors.userRole_XPATH).click()
        time.sleep(1)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.adminDD_XPATH).text == "Admin"
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.essDD_XPATH).text == "ESS"
        print("Admin and ESS are present within the dropdowns")
        print("Clicking on the Status Dropdown Menu")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.Status_XPATH).click()
        time.sleep(1)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.enabledDD_XPATH).text == "Enabled"
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.disabledDD_XPATH).text == "Disabled"
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
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.userCreTog_XPATH).click() #Toggle Button
        print("Click on Toggle was successful")
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_firstname).send_keys(data.Sumukh_Data.firstName) #Fill First Name
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.NAME, value=data.Sumukh_Selectors.input_box_lastname).send_keys(data.Sumukh_Data.lastName) #Fill Last Name
        time.sleep(data.Sumukh_Data.smallWait)
        self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.newUsername_XPATH).send_keys(data.Sumukh_Data.new_user) #Username
        self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.newPass_XPATH).send_keys(data.Sumukh_Data.new_pass) #Password
        self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.newConPass_XPATH).send_keys(data.Sumukh_Data.new_pass) #Confirm Password
        #Clicking on Enabled Button
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.enabledBut_XPATH).click() #Enabled Radio Button
        #Click on Save
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.saveUsrCre_XPATH).click()
        time.sleep(data.Sumukh_Data.longWait)
        print("Click on Save was successful")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.menuHead_XPATH).text == "Personal Details"
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
        self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.editIcon_XPATH).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.menuHead_XPATH).text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.persDet_XPATH).text == "Personal Details"
        print("Personal Details is present")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.contDet_XPATH).text == "Contact Details"        
        print("Contact Details is present")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.emerCon_XPATH).text == "Emergency Contacts"        
        print("Emergency Contacts is present")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.depen_XPATH).text == "Dependents"        
        print("Dependents is present")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.imig_XPATH).text == "Immigration"        
        print("Immigration is present")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.job_XPATH).text == "Job"        
        print("Job is present")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.salary_XPATH).text == "Salary"        
        print("Salary is present")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.taxExm_XPATH).text == "Tax Exemptions"        
        print("Tax Exemptions is present")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.repTo_XPATH).text == "Report-to"        
        print("Report-to is present")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.qual_XPATH).text == "Qualifications"        
        print("Qualifications is present")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.memb_XPATH).text == "Memberships"        
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
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.editIcon_XPATH).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.menuHead_XPATH).text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        #Click on Male Radio Button 
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.gen_XPATH).click()#Gender
        time.sleep(1)
        #Select Nationality
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.nationDD_XPATH).click()#Click on Nationality dropdown
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.indian_XPATH).click()#Nationality - Indian
        time.sleep(1)
        #Select Date of Birth
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.dob_XPATH).send_keys(data.Sumukh_Data.dob)#Date Picker
        time.sleep(1)
        #Enter SSN
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.ssn_XPATH).send_keys(data.Sumukh_Data.ssn)#SSN
        time.sleep(1)
        #Enter Marital Status
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.maritaldd_XPATH).click()#Click on the dropdown of marital status
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.singleStat_XPATH).click()#Select Single
        time.sleep(1)
        #Save all Personal Details
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.savePerDet_XPATH).click() #First Save
        time.sleep(10)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.ssn_XPATH).get_attribute('value') == data.Sumukh_Data.ssn #SSN
        print("SSN is validated")
        #assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.nationDD_XPATH).text == data.Sumukh_Data.nationality #Nationality
        print("Nationality is validated")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.maritaldd_XPATH).text == data.Sumukh_Data.marStatus #Marital Status
        print("Marital Status is validated")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.dob_XPATH).get_attribute('value') == data.Sumukh_Data.dob #DOB
        print("Date of Birth is validated")
        
    
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
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.editIcon_XPATH).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.menuHead_XPATH).text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.contDet_XPATH).click()
        time.sleep(3)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.menuHead_XPATH).text == "Contact Details"
        print("SUCCESS # Contact details is opened for the employee")
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.street1_XPATH).send_keys("Bangalore") #Street1
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.state_XPATH).send_keys("Karnataka") #State
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.country_XPATH).click()#Click on Country dropdown
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.counInd_XPATH).click()#Country - India
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.mobNum_XPATH).send_keys("123456789")#Home Number
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.email_XPATH).send_keys("project@AT.com")#Email
        time.sleep(1)
        #Click on Save
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.saveConDet_XPATH).click()
        time.sleep(5)
        assert self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.street1_XPATH).get_attribute('value') == "Bangalore" #Street1
        print("Street Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.state_XPATH).get_attribute('value') == "Karnataka" #State
        print("State Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.country_XPATH).text == "India" #Country
        print("Country Asserted")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.mobNum_XPATH).get_attribute('value') == "123456789" #Home Number
        print("Home Contact Asserted")
        assert self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.email_XPATH).get_attribute('value') == "project@AT.com"#Email
        print("Email ID Asserted")
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
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.editIcon_XPATH).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.menuHead_XPATH).text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.emerCon_XPATH).click()
        print("Clicked on Emergency Contact")
        time.sleep(6)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.newMenuHead_XPATH).text == "Assigned Emergency Contacts"
        print("SUCCESS # Emergency Contact details is opened for the employee")
        #Clicking on Add button
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.addBut_XPATH).click()
        time.sleep(5)
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.menuHead_XPATH).text == "Save Emergency Contact"
        #Enter Name
        self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.nameVal_XPATH).send_keys("Scale")
        time.sleep(1)
        #Enter Relationship
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.rel_XPATH).send_keys("Friend")
        time.sleep(1)
        #Enter Mobile Number
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.emPhon_XPATH).send_keys("123456789")
        time.sleep(2)
        #Click on Save
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.saveEmCo_XPATH).click()
        time.sleep(6)
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.emName_XPATH).text == "Scale"
        print("Name is successfully asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.emRel_XPATH).text == "Friend"
        print("Relationship is successfully asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.emPhNum_XPATH).text == "123456789"
        print("Mobile is successfully asserted")

    #TC_PIM_08 : Updating Employee Dependents Contact details Page post user creation.
    def test_TC_Login_08(self, booting_function):
        print("Test Objective : Updating Employee Dependents Contact details Page post user creation.")
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
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.editIcon_XPATH).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.menuHead_XPATH).text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.depen_XPATH).click()
        print("Clicked on Dependents")
        time.sleep(6)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.newMenuHead_XPATH).text == "Assigned Dependents"
        print("SUCCESS # Dependents details is opened for the employee")
        #Clicking on Add button
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.addButton_XPATH).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.nameVal_XPATH).send_keys("Jack") #Name of Dependent
        time.sleep(1)
        #Select Relationship
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.edRel_XPATH).click() #Click on the dropdown
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.edRelDDXPATH).click() #Select Child.
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.edDOB_XPATH).send_keys("2000-12-12")#DOB
        time.sleep(2)
        #Clicking on Save
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.saveEmCo_XPATH).click()#Click on Save
        time.sleep(6)
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.fced_XPATH).text == "Jack"
        print("Name is successfully asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.sced_XPATH).text == "Child"
        print("Relationship is successfully asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.tced_XPATH).text == "2000-12-12"
        print("DOB is successfully asserted")        

    #TC_PIM_09 : Updating Employee Job Details Page.
    def test_TC_Login_09(self, booting_function):
        print("Test Objective : Updating Employee Job Details Page.")
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
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.editIcon_XPATH).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.menuHead_XPATH).text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.job_XPATH).click()
        time.sleep(6)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.menuHead_XPATH).text == "Job Details"
        print("Clicked on Job Details.")
        print("SUCCESS # Job details is opened for the employee")
        #Enter Joining Date
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.joinDate_XPATH).send_keys("2020-01-01") #Enter Joining Date
        time.sleep(1)
        #Select Job Title
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.jobTitle_XPATH).click()
        time.sleep(1)
        #select from dropdown
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.edRelDDXPATH).click()#Selected Dropdown value
        time.sleep(1)
        #select Job Category
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.jobCat_XPATH).click() #Select Job Category
        time.sleep(1)
        #Select from Dropdown
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.jobCatDD_XPATH).click() #Craft Workers
        time.sleep(1)
        #select Sub Unit
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.subUnit_XPATH).click() #sub unit
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.adminstr_XPATH).click() #selected Administration
        time.sleep(1)
        #Select Location
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.loc_XPATH).click()
        time.sleep(1)
        #select from location dropdown
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.locDD_XPATH).click() #Canadian Regional HQ
        time.sleep(1)
        #select Employment Status
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.empStat_XPATH).click() #EMP STatus
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.empStatDD_XPATH).click() #Freelance
        time.sleep(1)
        #clicking on the toggle of Include Employment Contract Details
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.empCont_XPATH).click()
        time.sleep(2)
        #Enter Contract Start Date
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.contStart_XPATH).send_keys("2020-01-01")
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.contEnd_XPATH).send_keys("2021-01-01")
        time.sleep(2)
        #click on Save
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.savePerDet_XPATH).click()
        time.sleep(8)
        print("Asserting all values")
        assert self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.joinDate_XPATH).get_attribute('value') == "2020-01-01" #joining date
        print("Joining Date Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.jobTitle_XPATH).text == "Account Assistant"
        print("Role Asserted")
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.jobCat_XPATH).text == "Craft Workers"
        print("Work Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.subUnit_XPATH).text == "Administration"
        print("Administration Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.loc_XPATH).text == "Canadian Regional HQ"
        print("Region Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.empStat_XPATH).text == "Freelance"
        print("EMP Stat Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.contStart_XPATH).get_attribute('value') == "2020-01-01"
        print("Contract Start Date Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.contEnd_XPATH).get_attribute('value') == "2021-01-01"
        print("Contract End Date Asserted")

        print("All Values Asserted Successfully")

    #TC_PIM_10 : Updating Employee Job details Page post user creation.
    def test_TC_Login_10(self, booting_function):
        print("Test Objective : Updating Employee Job details Page post user creation.")
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
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.editIcon_XPATH).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.menuHead_XPATH).text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.job_XPATH).click()
        time.sleep(6)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.menuHead_XPATH).text == "Job Details"
        print("SUCCESS # Employee job details is opened for the employee")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.termActEmpl_XPATH).click() #Click on Terminate Employment
        time.sleep(5)
        print("Terminate Employment window is opened.") 
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.doterm_XPATH).send_keys("2021-01-01")
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.terRes_XPATH).click() #Clicking on Terminate Reason Dropdown
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.terOpt_XPATH).click() #Clicking on the options
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.terSave_XPATH).click() #Click on Save
        time.sleep(8)
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.terMes_XPATH).text == "Terminated on: 2021-01-01"   
        print("Terminated Message Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.termActEmpl_XPATH)
        print("Employee Terminated Successfully")
        #Continuing to execute TC_PIM_11 Test Case inside this block since Activation of the Emplpoyee is required.
        print("Executing TC_PIM_11 in this test case")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.termActEmpl_XPATH).click() #Activating the Employee
        time.sleep(5)
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.termActEmpl_XPATH) #Terminate Employement is present which means the Employee is activated.
        print("Employee Activated Successfully")

    #TC_PIM_12 : Updating Employee Salary details Page post user creation.
    def test_TC_Login_12(self, booting_function):
        print("Test Objective : Updating Employee Salary details Page post user creation.")
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
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.editIcon_XPATH).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.menuHead_XPATH).text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.salary_XPATH).click()
        time.sleep(8)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.newMenuHead_XPATH).text == "Assigned Salary Components"
        print("SUCCESS # Emergency Salary details is opened for the employee")
        #click on Add
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.addBut_XPATH).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.nameVal_XPATH).send_keys("AGC")
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.payFreq_XPATH).click() #Pay Frequency Dropdown
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.payFreqDD_XPATH).click() #Monthly
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.jobCat_XPATH).click() #Currency Drop Down
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.jobCatDD_XPATH).click() #USD
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.amVal_XPATH).send_keys("55000") #Amount
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.ddTogBt_XPATH).click() #Direct Deposit Toggle Button
        time.sleep(3)
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.accNum_XPATH) #Account Number
        print("Account Number Field Assserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.accTy_XPATH) #Account Type
        print("Account Type Field Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.rotNum_XPATH) #Routing Number
        print("Routing Number Field Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.rotAmt_XPATH) #Amount
        print("Amount Field Asserted")
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.accNumVal_XPATH).send_keys("9999999999") #Account Number
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.actv_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.actvDD_XPATH).click() #Savings
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.rtNum_XPATH).send_keys("1234") #Rounting Number
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.ddAMT_XPATH).send_keys("55000")#Amount
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.newSaveBut_XPATH).click()#Save
        time.sleep(150)
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.fced_XPATH).text == "AGC" #Salary Component
        print("Salary Value Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.sced_XPATH).text == "55000" #Amount
        print("Amount Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.tced_XPATH).text == "Afghanistan Afghani" #Currency
        print("Currency Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.monFD_XAPTH).text == "Monthly" #Frequency
        print("Frequency Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.monAMT_XPATH).text == "55000.00" #Direct Amount
        print("Total Amount Asserted")
        
    #TC_PIM_13 : Updating Employee Salary on Tax Exemption details Page post user creation.
    def test_TC_Login_13(self, booting_function):
        print("Test Objective : Updating Employee Salary on Tax Exemption details Page post user creation.")
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
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.editIcon_XPATH).click()
        time.sleep(data.Sumukh_Data.mediumWait)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.menuHead_XPATH).text == "Personal Details"
        print("SUCCESS # Employee List is opened for the employee")
        self.driver.find_element(by=By.XPATH, value =data.Sumukh_Selectors.taxExmpt_XPATH).click()
        time.sleep(8)
        assert self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.menuHead_XPATH).text == "Tax Exemptions"
        print("SUCCESS # Tax Exemption details is opened for the employee")
        #click on Status
        self.driver.find_element(by=By.XPATH, value= data.Sumukh_Selectors.taxStat_XPATH).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.taxStatDD_XPATH).click() #Single
        time.sleep(1)
        #Click on State       
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.taxState_XPATH).click()
        time.sleep(1)

        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.txStVal_XPATH).click() #Albama
        time.sleep(1)

        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.txStatVD_XPATH).click()
        time.sleep(1)

        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.txStatVDVal_XPATH).click() #Single
        time.sleep(1)
        #Unemployment Status
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.txStateVal_XPATH).click()
        time.sleep(1)

        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.albama_XPATH).click()#Albama
        time.sleep(1)
        #Work State
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.ddAlb_XPATH).click()
        time.sleep(1)

        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.albSec_XPATH).click() #Albama
        time.sleep(1)
        #Exemptions
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.rel_XPATH).send_keys("50")#50
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value = data.Sumukh_Selectors.fifty_XPATH).send_keys("50")#50
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.secSave_XPATH).click()
        print("Asserting all fields")
        time.sleep(8)
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.firCol_XPATH).text == "Single"
        print("Filed 1 Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.secCol_XPATH).text == "Alabama"
        print("State Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.txStatVD_XPATH).text == "Single"
        print("Single Value Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.txStateVal_XPATH).text == "Alabama"
        print("State Asserted")
        assert self.driver.find_element(by=By.XPATH, value=data.Sumukh_Selectors.ddAlb_XPATH).text == "Alabama"
        print("State 2 Asserted")


