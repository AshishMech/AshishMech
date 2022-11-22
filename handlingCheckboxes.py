# selecting all the checkboxes
from datetime import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
chrome_obj = webdriver.Chrome(service=service_obj)
chrome_obj.get("https://itera-qa.azurewebsites.net/home/automation")
checkboxes = chrome_obj.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")

# for checkbox in checkboxes:
#     checkbox.click()
#     time.sleep(1)

for i in range(len(checkboxes)):
    checkboxes[i].click()
    time.sleep(1)

time.sleep(5)
chrome_obj.quit()
