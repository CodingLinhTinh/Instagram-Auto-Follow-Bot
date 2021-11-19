from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import InstaFollower

#Your IG
username = ''
password = ''

#Acc that you want to get follow
acc_follower = ''

chrome_driver_path = ''
ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service = ser)



#Run the project
ins = InstaFollower(driver)

#Login
ins.login(username,password)

#follow
def find_followers_and_follow():
    ins.find_followers(acc_follower)
    ins.follow()
    
#unfollow
def unfollow_my_followers():
    ins.goto_profile(username)
    ins.unfollow()
