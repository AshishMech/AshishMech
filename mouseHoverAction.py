import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.get("https://learn.myquantic.com/")
Customer = driver.find_element(By.LINK_TEXT, "For Customers")
Business = driver.find_element(By.LINK_TEXT, "Business Type")
Restaurant = driver.find_element(By.XPATH, "/html/body/div/header/div/div/div/div/div[3]/div/nav/div/ul/li[1]/ul/li[1]/ul/li[1]/a")

# MouseHover
Hover = ActionChains(driver)

Hover.move_to_element(Customer).move_to_element(Business).move_to_element(Restaurant).click().perform()



