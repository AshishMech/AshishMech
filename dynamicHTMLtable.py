import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
time.sleep(4)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
time.sleep(4)

driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active']").click()
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span/i").click()
driver.find_element(By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-link']").click()
