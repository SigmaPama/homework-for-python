from time import sleep
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid")
blue_click = driver.find_element(By.CSS_SELECTOR, "button.btn")
blue_click.click()
sleep(5)
driver.quit()