
import time

from selenium import webdriver

driver = webdriver.Chrome('drivers/chromedriver')
driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(10)
driver.quit()
