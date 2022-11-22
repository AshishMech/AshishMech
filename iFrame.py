from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.XPATH, "//a[@class='analystic' and @href ='#Multiple']").click()

outerFrame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerFrame)

innerFrame = driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(innerFrame)

driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("you have mastered selenium")