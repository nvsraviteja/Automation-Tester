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
    if month == "February" and year == "2026":
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w'][1]").click()

noc = len(driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr[1]/td"))
nor = len(driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td[1]"))

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in dates:
    if date.text == "15":
        date.click()

# for r in range (nor):
#     for c in range (noc):
#         date = driver.find_element(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr["+str(r)+"]/td["+str(c)+"]/a")
#         if date == "15":
#             date.click()

c_date = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div").text

print (c_date)

input("enter")