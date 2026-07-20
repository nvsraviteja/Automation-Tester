import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")    
driver.maximize_window()


cookies = driver.get_cookies()

for c in cookies:
    print(c)
    