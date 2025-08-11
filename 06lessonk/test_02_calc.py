import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
print(ChromeDriverManager().install())

driver = webdriver.Chrome()
@pytest.fixture
def test_calcul():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.implicitly_wait(4)
    input_txt = driver.find_element(By.CSS_SELECTOR, "#delay").click()
    input_txt.send_keys("45")
    first_counter = driver.find_element(By.XPATH, "//*[contains(text(),'7')]").click()
    plus = driver.find_element(By.XPATH, "//*[contains(text(),'+')]").click()
    second_counter = driver.find_element(By.XPATH, "//*[contains(text(),'8')]").click()
    equal = driver.find_element(By.XPATH, "//*[contains(text(),'=')]").click()
    assert WebDriverWait(driver, 45).until(EC.visibility_of_element_located((By.LINK_TEXT, "15"))
    )