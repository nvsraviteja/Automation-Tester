from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

wait = WebDriverWait(driver, 10)

wait.until(
    EC.visibility_of_element_located((By.NAME, "username"))
).send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

wait.until(EC.title_contains("OrangeHRM"))

actual_title = driver.title
expected_title = "OrangeHRM"

if actual_title == expected_title:
    print("Test Passed")
else:
    print("Test Failed")

driver.quit()