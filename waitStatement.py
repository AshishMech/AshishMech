# implicit wait command

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
chromeDriver_obj = webdriver.Chrome(service=service_obj)
chromeDriver_obj.implicitly_wait(5)

chromeDriver_obj.get("https://www.google.com/")
search_obj = chromeDriver_obj.find_element(By.XPATH, "//input[@class='gLFyf gsfi']")
search_obj.send_keys("learn.myquantic.com")
search_obj.submit()

chromeDriver_obj.find_element(By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md']").click()







