import time
from selenium import webdriver
import os

#method for setup
global driver
Driver_Path=(os.getcwd().replace("Rought","").replace("\\","/")+"Drivers")
driver=webdriver.Chrome(executable_path=Driver_Path + "/chromedriver.exe")
driver.get("http://localhost:55555/login.do")
driver.maximize_window()
driver.implicitly_wait(30)

#method for login

driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_name("pwd").send_keys("manager")
driver.find_element_by_xpath("//div[text()='Login ']").click()

button=driver.find_element_by_xpath("//div[@class='buttonText' and text()='Add User']").is_displayed()
print(button)
# if button != "True":
#     time.sleep(5)
#     driver.find_element_by_xpath("//div[@class='label' and text()='USERS']").click()
#     driver.find_element_by_xpath("//div[@class='buttonText' and text()='Add User']").click()
#     F_N=driver.find_element_by_id("userDataLightBox_firstNameField").send_keys("Santhosh")
#     MID_N=driver.find_element_by_id("userDataLightBox_middleNameField").send_keys("NS")
#     L_N=driver.find_element_by_id("userDataLightBox_lastNameField").send_keys("Kumar")
#     driver.find_element_by_id("userDataLightBox_emailField").send_keys("abc@abc.com")
#     driver.find_element_by_id("userDataLightBox_usernameField").send_keys("san")
#     driver.find_element_by_id("userDataLightBox_passwordField").send_keys("san123")
#     driver.find_element_by_id("userDataLightBox_passwordCopyField").send_keys("san123")
#     driver.find_element_by_id("userDataLightBox_commitBtn").click()
# else:
driver.find_element_by_xpath("//input[@class='filterFieldInput inputFieldWithPlaceholder']").send_keys("Santhosh")
driver.find_element_by_xpath("//span[text()='Santhosh']").click()
driver.find_element_by_xpath("//button[@id='userDataLightBox_deleteBtn']").click()
b=driver.find_element_by_name("alert")
b.click()