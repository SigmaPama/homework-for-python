import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

@pytest.fixture

def test_shop():
    driver.get("https://www.saucedemo.com/")
    
    username = driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    
    password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    
    login_button = driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    driver.implicitly_wait(7)
    
    back_pack = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    
    t_shirt = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    
    onesie = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    
    cart_link = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    driver.implicitly_wait(7)
    check_out = driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    driver.implicitly_wait(4)
    
    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Den")
    
    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Tralale")
    
    post_code = driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123554")
    
    press_contine = driver.find_element(By.CSS_SELECTOR, "#continue").click()
    driver.implicitly_wait(4)
    
    total_price = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    print(total_price)
    driver.quit()
    assert total_price == "$58.29"

