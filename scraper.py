from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys

driver = webdriver.Chrome()

driver.get(sys.argv[1])

print(driver.title)
search_bar = driver.find_element(by=By.NAME, value="q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)


driver.close()
