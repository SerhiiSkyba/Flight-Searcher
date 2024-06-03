from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

# Set Firefox options
firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

# Initialize webdriver with Firefox
driver = webdriver.Firefox(options=firefox_options)

# Set URL and date of travel
url = 'https://www.google.com/travel/flights?tfs=CBwQARocagwIAxIIL20vMDg0NWJyDAgEEggvbS8wMmo3MRocagwIBBIIL20vMDJqNzFyDAgDEggvbS8wODQ1YkABSAFwAYIBCwj___________8BmAEB&tfu=KgIIAw'
date_of_travel = "2023-04-22"

# Print URL
print(f"URL: {url}")

# Load webpage
driver.get(url)


time.sleep(5)

a = driver.find_element(By.CLASS_NAME, "lssxud")
a.click()

search_button = driver.find_element(By.CLASS_NAME, "xFFcie")
search_button.click()
