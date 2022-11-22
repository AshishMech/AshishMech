from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")

driver = webdriver.Chrome(service=serv_obj)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")

for checkbox in checkboxes:
    checkbox.click()

time.sleep(3)


for checkbox in checkboxes:
    checkbox.click()
