import pytest
from CaclClass import Calc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager




def test_calc():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    first_step = Calc(browser)
    first_step.wait_for("45")
    first_step.tap_buttons("7", "+", "8", "=")
    first_step.save_result()