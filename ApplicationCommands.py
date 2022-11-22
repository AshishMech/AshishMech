from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.in/")
act_title = driver.title
exp_title = "Amazon.in"

if act_title == exp_title:
    print("the title seems correct")

else:
    print("exp and actual title are different")
    print(act_title)

driver.quit()




