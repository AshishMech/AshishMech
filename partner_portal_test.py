from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver.get("https://dev-partnerportal.metispro.com/")
driver.find_element(By.NAME, "loginemailid").send_keys("codeadmin@metispro.com")
driver.find_element(By.NAME, "loginpassword").send_keys("Chke2019@")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

//button[@type='submit']