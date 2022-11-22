from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://dev-portal.metispro.com/")
driver.find_element(By.ID, "userName").send_keys("10110842")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.XPATH, '//*[@id="login"]').click()
driver.implicitly_wait(7)
driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div[1]/a[1]/i").click()
driver.find_element(By.XPATH, "/html/body/div[10]/nav/ul/li[3]/a/i").click()
driver.implicitly_wait(5)
categoryDrop = driver.find_element(By.XPATH, '//*[@id="category"]')
Options = Select(categoryDrop)
# Options.select_by_index(4)
Options.select_by_visible_text("Deposit Category")