from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
