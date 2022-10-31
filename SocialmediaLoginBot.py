#Importing all the necessary selenium lib after pip installing selenium in command propmt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time


#Creating a login bot using selenium
#Adding your Eamil Credentials for Login
socialmedia_mail = "#enter email id"
socialmedia_pass = "#enter pass"

#Setting up Chrome driver path 
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#URL of the website and webpage we want to visit
driver.get("Enter the url of social media website")


#Inspecting the email feild
email =  driver.find_element(By.NAME, "email")
email.send_keys(socialmedia_mail)

#Inspecting the password feild
password = driver.find_element(By.NAME, "password")
password.send_keys(socialmedia_pass)
password.send_keys(Keys.RETURN)

#login button will be clicked by entering the xpath of the button
driver.find_element(By.XPATH("#xpath of the button to be entered")).click();
