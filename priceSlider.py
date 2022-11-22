from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/metispro/Downloads/chromedriver_linux64 (1)/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
min_slider = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/span[1]")  #{'x': 59, 'y': 250}
max_slider = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/span[2]")  #{'x': 401, 'y': 250}

print(".............location of min and max before sliding")
print(min_slider.location)
print(max_slider.location)
print()


action_obj = ActionChains(driver)
action_obj.drag_and_drop_by_offset(min_slider, 10, 0).perform()
action_obj.drag_and_drop_by_offset(max_slider, -100, 0).perform()

print("location of min and max after sliding..............")
print(min_slider.location)
print(max_slider.location)

min_field = driver.find_element(By.XPATH, "//*[@id='min_price']")
print(min_field.text)

max_field = driver.find_element(By.XPATH, "//*[@id='max_price']")
print(max_field.text)

