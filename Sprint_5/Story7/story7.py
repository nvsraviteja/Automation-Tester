from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

# driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/button").click()

# alert = driver.switch_to.alert
# alert.send_keys("admin")
# print(alert.text)
# alert.accept()
# 
has = input("enter")

