from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

# printing all the books written by Mukesh

driver.get("https://testautomationpractice.blogspot.com/")
rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tbody/tr"))


for M in range(2, rows+1):
    Author = driver.find_element(By.XPATH, "//table[@name='BookTable']//tbody/tr["+str(M)+"]/td[2]").text
    if Author == "Mukesh":
        BookName = driver.find_element(By.XPATH, "//table[@name='BookTable']//tbody/tr["+str(M)+"]/td[1]").text

        Subject = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(M)+"]/td[3]").text
        print(BookName, "  ", Subject)



        # Books = driver.find_element(By.XPATH, "//table[@name='BookTable']//tbody/tr/td[1]").text
        # print(Books)
