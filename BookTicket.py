from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=service_obj)
myWait = WebDriverWait(driver, 10)


driver.get("https://www.easemytrip.com/")
driver.find_element(By.XPATH, "//p[@id='pff']").click()
driver.find_element(By.XPATH, "//input[@id='a_FromSector_show']").send_keys('BOM')
driver.find_element(By.XPATH, "//p[@id='ptt']").click()
driver.find_element(By.XPATH, "//input[@id='a_Editbox13_show']").send_keys('DEL')

driver.find_element(By.ID, "ddate").click()
driver.find_element(By.XPATH, "//*[@id='fiv_2_27/09/2022']").click()
driver.find_element(By.XPATH, "//*[@id='showOWRT']/div/div[7]/button").click()

searchlink = myWait.until(EC.presence_of_element_located(By.XPATH, "//button[@class='btn book-bt-n ng-scope']"))
searchlink.click()
# driver.find_element(By.XPATH, "//button[@class='btn book-bt-n ng-scope']").click()

