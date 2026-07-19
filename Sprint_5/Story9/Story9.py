import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")    
driver.maximize_window()


nor=driver.find_elements(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr")
print("Number of rows in the table are: ",len(nor))
noc = driver.find_elements(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th")
print("Number of columns in the table are: ",len(noc))

for r in nor:
    if "Mukesh" in r.text:
        print(r.text)
        print("Row number is: ",nor.index(r)+1)

