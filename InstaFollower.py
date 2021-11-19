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
        
        
    def find_followers(self,acc_follower):
        time.sleep(1)
        self.driver.get(f"https://www.instagram.com/{acc_follower}")
        
        #click 'Follower'
        time.sleep(2)
        followers = self.driver.find_element(By.CSS_SELECTOR, 'ul li a')
        followers.click()
        
        #scrolling insise poppup
        modal = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
        
        
    def follow(self):
        count=0
        
        #get follow button
        all_buttons = self.driver.find_elements(By.XPATH, "//button[contains(.,'Follow')][not(contains(.,'Following'))]")
        for button in all_buttons:
            self.driver.execute_script("arguments[0].click();", button)
            print('Followed')
            
            count += 1
            time.sleep(1)
            #You cannot un/follow more than 50
            if count == 50:
                break
                
                
    def goto_profile(self, username):
        time.sleep(1)
        self.driver.get(f"https://www.instagram.com/{username}")
        time.sleep(2)
        
        following = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        following.click()
        
        #scrolling inside poppup
        popup = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[3]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
            time.sleep(2)
        
        
    def unfollow(self):
        count=0
        #get Following button
        unfollow_buttons = driver.find_elements(By.XPATH, "//button[contains(.,'Following')]")
        
        for button in unfollow_buttons:
            self.driver.execute_script("arguments[0].click();", button)
            time.sleep(3)
           
            unfollow_button = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[1]")
            unfollow_button.click()
            time.sleep(3)
            print('UnFollowed')
            
            #You cannot un/follow more than 50
            count+=1
            if count == 50:
                break
