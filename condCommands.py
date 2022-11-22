from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
cdriver = webdriver.Chrome(service=service_obj)

cdriver.get("https://www.snapdeal.com/")
search = cdriver.find_element(By.XPATH, "//input[@name = 'keyword']")
search.send_keys("apple")
print(search.get_attribute('id'))


