from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
search_box = driver.find_element(By.CSS_SELECTOR, "#username")
search_box.send_keys("tomsmith")
search_box = driver.find_element(By.CSS_SELECTOR, "#password")
search_box.send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, ".fa").click()
green = driver.find_element(By.CSS_SELECTOR, ".flash.success")
print(f'{green}')
sleep(500)
driver.quit()