
from time import sleep
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
print(ChromeDriverManager().install())

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")
driver.find_element(By.CSS_SELECTOR, ("button.btn-primary")).click()

sleep(5)

driver.quit()
