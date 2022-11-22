from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
Button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
right_click = ActionChains(driver)
right_click.context_click(Button).perform()
driver.find_element(By.XPATH, "/html/body/ul/li[3]").click()
driver.switch_to.alert.accept()
