# selecting only tuesday and saturday

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

s_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=s_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")

for i in checkboxes:
    week = i.get_attribute('id')
    if week == 'monday' or week == 'wednesday':
        i.click()

