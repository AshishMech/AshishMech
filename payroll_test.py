from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver.get("https://onex.osourceglobal.com/ONEX-NEXGEN/Login.aspx")
driver.find_element(By.NAME, 'Login1$CompanyCode').send_keys("FIITJ")
driver.find_element(By.NAME, 'Login1$UserName').send_keys("37739")
driver.find_element(By.NAME, 'Login1$Password').send_keys("Fiitjee@123")

driver.find_element(By.ID, 'Login1_LoginButton').click()

# driver.find_element(By.ID, 'password').send_keys("B@dola1989")
# driver.find_element(By.ID, 'login').click()

# act_title = driver.title
# exp_title = "Dashboard"
#
# if act_title == exp_title:
#     print("login test pass")
#
# else:
#     print("login test failed")
#
# driver.close()
