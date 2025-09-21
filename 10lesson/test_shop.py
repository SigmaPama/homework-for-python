import pytest
import allure
from shop_page import Autorization
from shop_page import MainPage
from shop_page import ScoreItem
from shop_page import PostalAndCheck
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест процесса покупки в интернет-магазине")
@allure.description("Проверка полного цикла покупки: авторизация, добавление товаров, оформление заказа")
def test_shop():
    with allure.step("Инициализация браузера"):
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    
    with allure.step("Авторизация в системе"):
        auto = Autorization(browser)
        auto.autorize("standard_user", "secret_sauce")
    
    with allure.step("Добавление товаров в корзину"):
        click_item = MainPage(browser)
        click_item.take_items()
    
    with allure.step("Переход к оформлению заказа"):
        items = ScoreItem(browser)
        items.checkout()
    
    with allure.step("Ввод данных для оформления заказа"):
        total_score = PostalAndCheck(browser)
        total_score.input_info("Den", "Tartilia", "235786")
    
    with allure.step("Проверка общей суммы заказа"):
        total_price = total_score.get_total_price()
        assert "$58.29" in total_price
    
    with allure.step("Закрытие браузера"):
        browser.quit()