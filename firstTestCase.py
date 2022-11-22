from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")

driver = webdriver.Chrome(service=service_obj)
driver.get("https://dev-portal.metispro.com/")
driver.find_element(By.NAME, 'userName').send_keys("10110842")
driver.find_element(By.ID, 'password').send_keys("123456")
driver.find_element(By.ID, 'login').click()
act_title = driver.title
exp_title = "Dashboard"

if act_title == exp_title:
    print("login test pass")

else:
    print("login test failed")

driver.close()