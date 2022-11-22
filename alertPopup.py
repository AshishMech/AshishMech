from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element(By.CLASS_NAME, "signinbtn").click()
alert_obj = driver.switch_to.alert
alert_obj.accept()

driver.find_element(By.ID, "login1").send_keys("bqjb")
driver.find_element(By.ID, "password").send_keys("bqjbfbufbwifnwfkj")
driver.find_element(By.CLASS_NAME, "signinbtn").click()

