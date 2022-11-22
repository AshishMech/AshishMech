from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(5)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
source = driver.find_element(By.XPATH, "//div[@id='box4']")
target = driver.find_element(By.XPATH, "//div[@id='box103']")

action_obj = ActionChains(driver)
action_obj.drag_and_drop(source, target).perform()
