from selenium import webdriver

# Selenium automatically finds, downloads, and matches ChromeDriver to your Chrome version
driver = webdriver.Chrome()

# Open a website
driver.get("https://google.com")

# Print the page title
print(driver.title)

# Close the browser
driver.quit()