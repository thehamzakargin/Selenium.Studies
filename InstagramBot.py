from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def _init_(self,username,password): 
        self.browser = webdriver.Chrome()           
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)

        usernameInput = self.browser.find_element("xpath","//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element("xpath","//*[@id='loginForm']/div/div[2]/div/label/input")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(10)

        self.browser.get("https://www.instagram.com/thehamzakargin/followers/")
        time.sleep(10)
        # followersLink = self.browser.find_element("xpath","//*[@id='mount_0_0_jy']/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div")
        # followersLink.click()
        # time.sleep(10)
        followers = self.browser.find_element("cssSelector","div[role=dialog]")
        for user in followers:
            link = user.find_element("cssSelector","a").get_attribute("href")
            print(link)


instgrm = Instagram(username,password)
instgrm.signIn()