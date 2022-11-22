import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH, "//input[@id = 'Wikipedia1_wikipedia-search-input']").send_keys("selenium")
driver.find_element(By.CLASS_NAME, "wikipedia-search-button").click()
time.sleep(3)

five_browsers = driver.find_elements(By.XPATH, "//a[@target = '_blank' and contains(@href, "
                                               "'https://en.wikipedia.org/wiki/Selenium')]")

for browser in five_browsers:
    browser.click()


# driver.find_element(By.LINK_TEXT, "Selenium").click()
# driver.find_element(By.LINK_TEXT, "Selenium in biology").click()
# driver.find_element(By.LINK_TEXT, "Selenium (software)").click()
# driver.find_element(By.LINK_TEXT, "Selenium disulfide").click()
# driver.find_element(By.LINK_TEXT, "Selenium dioxide").click()

all_browsers = driver.window_handles

for browser in all_browsers:
    driver.switch_to.window(browser)
    print(driver.title)


driver.quit()
