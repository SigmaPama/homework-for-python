import pytest
import allure
from calculator_page import Calc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест работы калькулятора с задержкой")
@allure.description("Проверка вычисления 7 + 8 с установленной задержкой 45 секунд")
def test_calc():
    with allure.step("Инициализация браузера"):
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    
    with allure.step("Создание экземпляра калькулятора"):
        first_step = Calc(browser)
    
    with allure.step("Установка задержки вычисления"):
        first_step.set_delay("45")
    
    with allure.step("Выполнение операции 7 + 8"):
        first_step.tap_buttons("7", "+", "8", "=")
    
    with allure.step("Проверка результата вычисления"):
        first_step.save_result()
    
    with allure.step("Закрытие браузера"):
        browser.quit()