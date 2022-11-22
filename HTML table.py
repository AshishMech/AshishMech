from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
no_of_rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tbody//tr")
print(len(no_of_rows))


no_of_column = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tbody//th")
print(len(no_of_column))


