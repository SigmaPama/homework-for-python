import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType




def test_buttons():
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.implicitly_wait(4)
    
    first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
    
    last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
    
    address_input = driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
    
    
    email_address = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
    
    phone_number = driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
  
    
    city_name = driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Москва")

    country_name = driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")


    job_position = driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")

    company_name = driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")
  
    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary").click()
    
    zip_code = driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").value_of_css_property("border-color")
    assert zip_code == "rgba(255, 0, 0, 1)"
    green_elements = ["first_name", "last_name", "address", "email", "phone", "city", "country", "job", "company"]
    for taps in green_elements:
        taps = driver.find_elements(By.CSS_SELECTOR, ".form-label").value_of_css_property("background-color")
        assert taps == "#d1e7dd"