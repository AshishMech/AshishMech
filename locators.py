from itertools import count

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
Chrome_obj = webdriver.Chrome(service=Service_obj)

Chrome_obj.get("https://www.amazon.in/")
Chrome_obj.maximize_window()
Class_obj = Chrome_obj.find_elements(By.CLASS_NAME, "nav-a")
print(len(Class_obj))

