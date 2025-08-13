from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class Calc:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
    

    def wait_for(self,kye):
        self.wait = WebDriverWait(self._driver, 45)
        self.input_txt = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        self.input_txt.clear()
        self.input_txt.send_keys(kye)

    def tap_buttons(self, key1, key2, key3, key4):
            self._driver.find_element(By.XPATH, f"//span[normalize-space()='{key1}']").click()
            self._driver.find_element(By.XPATH, f"//span[normalize-space()='{key2}']").click()
            self._driver.find_element(By.XPATH, f"//span[normalize-space()='{key3}']").click()
            self._driver.find_element(By.XPATH, f"//span[normalize-space()='{key4}']").click()
    
    def save_result(self):
         self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
         assert self._driver.find_element(By.CSS_SELECTOR, "div.screen").text.strip() == "15"    
         self._driver.quit()     



    