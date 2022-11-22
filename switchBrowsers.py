from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://learn.myquantic.com/")
driver.find_element(By.LINK_TEXT, "For Customers").click()

windowIDs = driver.window_handles
print(len(windowIDs))
# parentWindow = windowIDs[0]
# childWindow = windowIDs[1]
# print(parentWindow, childWindow)

# driver.switch_to(childWindow)
#
# driver.switch_to(parentWindow)

