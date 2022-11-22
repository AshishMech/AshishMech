from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://dev-portal.metispro.com/")
driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("10110842")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456")
driver.find_element(By.XPATH, "//a[@id='login']").click()
driver.find_element(By.CLASS_NAME, "mp_ic_menu").click()
driver.find_element(By.CLASS_NAME, "mp_catalog-of-colors").click()

taxMenu = driver.find_element(By.ID, "taxClass")
Options = Select(taxMenu)

allOptions = Options.options
for eachOption in allOptions:
    if eachOption.text == "Tax ":
        eachOption.click()


# Options.select_by_visible_text("GST")

#
# allOptions = Options.options
# for eachOption in allOptions:
#     print(eachOption.text)







