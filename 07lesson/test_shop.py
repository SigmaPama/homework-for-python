import pytest
from ShopClass import Autorization
from ShopClass import MainPage
from ShopClass import ScoreItem
from ShopClass import PostalAndCheck
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager




def test_shop():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    auto = Autorization(browser)
    auto.autoriz("standard_user", "secret_sauce")
    click_item = MainPage(browser)
    click_item.take_items()
    items = ScoreItem(browser)
    items.CheckOut()
    total_score = PostalAndCheck(browser)
    total_score.input_info("Den", "Tartilia", "235786")
    total_score.check_prise()
    browser.quit()

