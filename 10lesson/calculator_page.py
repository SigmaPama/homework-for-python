from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class Calc:
    """Page Object класс для работы с калькулятором."""
    
    def __init__(self, driver):
        """
        Инициализация калькулятора.
        
        :param driver: WebDriver экземпляр для управления браузером
        :type driver: WebDriver
        """
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def set_delay(self, key):
        """
        Установка задержки вычисления.
        
        :param key: Значение задержки в секундах
        :type key: str
        :return: None
        """
        self.wait = WebDriverWait(self._driver, 45)
        self.input_txt = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        self.input_txt.clear()
        self.input_txt.send_keys(key)

    def tap_buttons(self, key1, key2, key3, key4):
        """
        Нажатие последовательности кнопок калькулятора.
        
        :param key1: Первая кнопка для нажатия
        :type key1: str
        :param key2: Вторая кнопка для нажатия
        :type key2: str
        :param key3: Третья кнопка для нажатия
        :type key3: str
        :param key4: Четвертая кнопка для нажатия
        :type key4: str
        :return: None
        """
        self._driver.find_element(By.XPATH, f"//span[normalize-space()='{key1}']").click()
        self._driver.find_element(By.XPATH, f"//span[normalize-space()='{key2}']").click()
        self._driver.find_element(By.XPATH, f"//span[normalize-space()='{key3}']").click()
        self._driver.find_element(By.XPATH, f"//span[normalize-space()='{key4}']").click()

    def save_result(self):
        """
        Сохранение и проверка результата вычисления.
        
        :return: None
        :raises AssertionError: Если результат не соответствует ожидаемому
        """
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
        assert self._driver.find_element(By.CSS_SELECTOR, "div.screen").text.strip() == "15"