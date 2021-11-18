from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import InstaFollower
#Your IG
username = ''
password = ''

#Acc that you want to follow
acc_follower = ''

chrome_driver_path = ''
ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service = ser)
                

#Run the project
ins = InstaFollower(driver)
ins.login(username,password)
ins.find_followers(similar_acc)
ins.follow()
