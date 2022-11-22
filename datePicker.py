from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://jqueryui.com/datepicker/")

frame = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")

driver.switch_to.frame(frame)
# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("06/13/1989")
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

month = 'June'
year = '2023'
date = '15'

while True:
    Month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    Year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if month == Month and year == Year:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

all_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for dates in all_dates:
    if dates.text == date:
        dates.click()
