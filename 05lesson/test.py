from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Проверка версий
print("Установка ChromeDriver...")
driver_path = ChromeDriverManager(version="138.0.7204.184").install()
print(f"Путь к драйверу: {driver_path}")

# Запуск
driver = webdriver.Chrome(service=ChromeService(driver_path))
driver.get("http://uitestingplayground.com/classattr")
driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
time.sleep(3)
driver.quit()
print("Тест завершён!")