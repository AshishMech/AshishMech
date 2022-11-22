from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
chrome_obj = webdriver.Chrome(service = service_obj)

chrome_obj.get("https://www.amazon.in/")
chrome_obj.find_element(By.CSS_SELECTOR, "span#nav-link-accountList-nav-line-1").click()
chrome_obj.find_element(By.XPATH, "//span[@class='nav-action-inner']").click()
chrome_obj.find_element(By.XPATH, "//*[@id='ap_email']").send_keys("8745008300")
chrome_obj.find_element(By.CSS_SELECTOR, "input#continue").click()
chrome_obj.find_element(By.ID, 'ap_password').send_keys('DEHRADUN@123')
chrome_obj.find_element(By.ID, 'signInSubmit').click()
chrome_obj.close()

