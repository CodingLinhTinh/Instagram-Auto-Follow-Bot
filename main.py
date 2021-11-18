from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

#Your IG
username = ''
password = ''

#Acc that you want to follow
acc_follower = ''

chrome_driver_path = ''
ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service = ser)

class InstaFollower:
    def __init__(self,driver):
        self.driver = driver
        
    def login(self,username,password):
        url = 'https://www.instagram.com/'
        self.driver.get(url)
        time.sleep(5)
        
        userinput = self.driver.find_element(By.NAME, 'username')
        passinput = self.driver.find_element(By.NAME, 'password')
        
        loginbutton = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        
        userinput.send_keys(username)
        passinput.send_keys(password)
        
        time.sleep(5)
        passinput.send_keys(Keys.ENTER)
        
    def find_followers(self,similar_acc):
        time.sleep(1)
        self.driver.get(f"https://www.instagram.com/{acc_follower}")

        time.sleep(2)
        followers = self.driver.find_element(By.CSS_SELECTOR, 'ul li a')
        followers.click()

        page = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", page)
            time.sleep(2)
        
    def follow(self):
        all_buttons = self.driver.find_elements(By.XPATH, "//button[contains(.,'Follow')][not(contains(.,'Following'))]")
        for button in all_buttons:
            try:
                self.driver.execute_script("arguments[0].click();", button)
                print('Followed')
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()
                

#Run the project
ins = InstaFollower(driver)
ins.login(username,password)
ins.find_followers(similar_acc)
ins.follow()
