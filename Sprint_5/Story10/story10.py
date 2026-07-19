import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")    
driver.maximize_window()

act = ActionChains(driver)

drag = driver.find_element(By.ID , "draggable")
drop = driver.find_element(By.ID, "droppable")

act.drag_and_drop(drag,drop).perform()

input('enter')