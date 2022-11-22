from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://learn.myquantic.com/")
driver.find_element(By.XPATH, "//a[@class='line_btn'] ").click()

all_windows = driver.window_handles
# parent_window = all_windows[0]
# child_window = all_windows[1]

# print(parent_window)
# print(child_window)

for windowsIDs in all_windows:
    driver.switch_to.window(windowsIDs)
    print(driver.title)
