# last 2 checkboxes

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

sobj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=sobj)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")

for i in range(len(checkboxes)-2, len(checkboxes)):
    checkboxes[i].click()
