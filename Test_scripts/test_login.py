import time
from selenium import webdriver
import os

#method for setup
def test_setup():
    global driver
    Driver_Path=(os.getcwd().replace("Test_scripts","").replace("\\","/")+"Drivers")
    driver=webdriver.Chrome(executable_path=Driver_Path + "/chromedriver.exe")
    driver.get("http://localhost:55555/login.do")
    driver.maximize_window()
    driver.implicitly_wait(30)

#method for login
def test_login():
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_name("pwd").send_keys("manager")
    driver.find_element_by_xpath("//div[text()='Login ']").click()
'''
button=driver.find_element_by_class_name("addUserButton beigeButton useNativeActive disabled").is_enabled()
print(button)

def test_newuser():
    time.sleep(5)
    driver.find_element_by_xpath("//div[@class='label' and text()='USERS']").click()
    driver.find_element_by_xpath("//div[@class='buttonText' and text()='Add User']").click()
    driver.find_element_by_id("userDataLightBox_firstNameField").send_keys("Santhosh")
    driver.find_element_by_id("userDataLightBox_middleNameField").send_keys("NS")
    driver.find_element_by_id("userDataLightBox_lastNameField").send_keys("Kumar")
    driver.find_element_by_id("userDataLightBox_emailField").send_keys("abc@abc.com")
    driver.find_element_by_id("userDataLightBox_usernameField").send_keys("san")
    driver.find_element_by_id("userDataLightBox_passwordField").send_keys("san123")
    driver.find_element_by_id("userDataLightBox_passwordCopyField").send_keys("san123")
    driver.find_element_by_id("userDataLightBox_commitBtn").click()
'''

#method for logout
def test_logout():
    time.sleep(5)
    driver.find_element_by_xpath("//a[text()='Logout']").click()
    driver.close()

test_setup()
test_login()
# test_newuser()
test_logout()
