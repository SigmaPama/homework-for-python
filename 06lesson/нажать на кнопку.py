from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.implicitly_wait(15)

driver.get("http://uitestingplayground.com/ajax")

tap_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

content_tap = driver.find_element(By.CSS_SELECTOR, "#content")

txt = content_tap.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(txt)
driver.quit()


