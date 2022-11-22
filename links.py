import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://learn.myquantic.com/")
driver.maximize_window()

allLinks = driver.find_elements(By.TAG_NAME, "a")
# print(len(allLinks))

count = 0
for link in allLinks:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url, " is broken link")
        count += 1

    else:
        print(url, " is a valid link")

print("total number of links are: ", count)
