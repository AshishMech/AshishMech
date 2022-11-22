from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://testautomationpractice.blogspot.com/')
Rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
Columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th"))

print(Rows, Columns)

for r in range(2, Rows + 1):
    for c in range(1, Columns + 1):
        data = driver.find_element(By.XPATH,
                                   "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(data, end='      ')

    print("    ")
