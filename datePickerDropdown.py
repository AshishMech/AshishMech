import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(By.ID, "dob").click()

# identify all the months in a dropdown

month_field = driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']")
all_months_obj = Select(month_field)
all_months_obj.select_by_value("5")

time.sleep(2)

# grab_month = all_months_obj.options

# for month in grab_month:
#     print(month.text)

# identify all the years in a dropdown

all_years = driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']")
all_years_obj = Select(all_years)
all_years_obj.select_by_value("1989")
time.sleep(2)


# identify date from the calender

date = "13"
all_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td")

for dates in all_dates:
    if dates.text == date:
        dates.click()
        break
time.sleep(1)

years = all_years_obj.all_selected_options
print(years)
