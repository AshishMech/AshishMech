import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.get("https://text-compare.com/")
input1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

input1.send_keys("Hello Ashish")

action_obj = ActionChains(driver)
action_obj.key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL).perform()
time.sleep(3)
action_obj.key_down(Keys.CONTROL).send_keys("C").key_up(Keys.CONTROL).perform()
time.sleep(3)
action_obj.key_down(Keys.TAB).key_up(Keys.TAB).perform()
time.sleep(3)
action_obj.key_down(Keys.CONTROL).send_keys("V").key_up(Keys.CONTROL).perform()
input1.clear()

