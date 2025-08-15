import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    service = FirefoxService(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    drv = webdriver.Firefox(service=service, options=options)
    drv.maximize_window()
    yield drv
    drv.quit()

def test_total_contains_58_29(driver):
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(7)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Ivan")
    driver.find_element(By.ID, "last-name").send_keys("Petrov")
    driver.find_element(By.ID, "postal-code").send_keys("101000")
    driver.find_element(By.ID, "continue").click()

    total_text = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text

    assert "$58.29" in total_text
