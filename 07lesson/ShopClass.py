from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class Autorization:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def autoriz(self, name, password ):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        self.driver.implicitly_wait(7)

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def take_items(self):
       self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
       self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
       self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
       self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
       self.driver.implicitly_wait(7) 

class ScoreItem:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def CheckOut(self,):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        self.driver.implicitly_wait(4)

class PostalAndCheck:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def input_info(self, first_name, last_name, post_code):
      self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
      self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
      self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(post_code)
      self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
      self.driver.implicitly_wait(4)  

    def check_prise(self):
        result = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        print(result)
        self.driver.quit()
        assert "$58.29" in result
