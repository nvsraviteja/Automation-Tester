import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")    
driver.maximize_window()


driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='content']/iframe"))

driver.find_element(By.XPATH, "//*[@id='datepicker']").click()  
c_date = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div").text

while True:
    month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if month == "March" and year == "2024":
        break
    elif year < "2026":
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w'][1]").click()

input("enter")