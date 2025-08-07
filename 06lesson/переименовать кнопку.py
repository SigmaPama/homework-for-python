from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")
my_button = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
my_button.send_keys("SkyPro")
blue_tap = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
after_tap = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(after_tap)
driver.quit()