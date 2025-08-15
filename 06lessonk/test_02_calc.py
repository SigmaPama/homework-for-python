import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

@pytest.fixture
def driver():
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    drv = webdriver.Chrome(service=service, options=options)
    drv.maximize_window()
    yield drv
    drv.quit()

def test_slow_calculator_45s(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 45) 

    delay = driver.find_element(By.ID, "delay")
    delay.clear()
    delay.send_keys("45")

    for key in ["7", "+", "8", "="]:
        driver.find_element(By.XPATH, f"//span[normalize-space()='{key}']").click()

    # Ждём появления "15" в экране калькулятора
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
    assert driver.find_element(By.CSS_SELECTOR, "div.screen").text.strip() == "15"
    