from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
button = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")
mouse_obj = ActionChains(driver)
mouse_obj.double_click(button).perform()
popup = driver.switch_to.alert
popup.accept()