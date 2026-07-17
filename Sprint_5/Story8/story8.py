import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")    
driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-input']").send_keys("Selenium")
driver.find_element(By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-form']/div/span[2]/span[2]/input").click()

time.sleep(3)

links = driver.find_elements(By.XPATH, "//*[@id='wikipedia-search-result-link']/a")  

for link in links:
    link.click()


all_windows = driver.window_handles

for window in all_windows:
    driver.switch_to.window(window)
    print(driver.title)
    if driver.title == "Selenium - Wikipedia" or driver.title == "Selenium in biology - Wikipedia":
        driver.close()

input("enter")
