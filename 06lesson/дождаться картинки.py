from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
 
waiter = WebDriverWait(driver, 15)
waiter.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR), "#landscape")
)
imag = driver.find_element(By.CSS_SELECTOR, "#award")
print(imag.get_attribute("src"))
driver.quit()

