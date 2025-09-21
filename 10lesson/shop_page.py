from selenium.webdriver.common.by import By

class Autorization:
    """Page Object класс для авторизации в интернет-магазине."""
    
    def __init__(self, driver):
        """
        Инициализация страницы авторизации.
        
        :param driver: WebDriver экземпляр для управления браузером
        :type driver: WebDriver
        """
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def autorize(self, name, password):
        """
        Выполнение авторизации.
        
        :param name: Имя пользователя
        :type name: str
        :param password: Пароль пользователя
        :type password: str
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        self.driver.implicitly_wait(7)

class MainPage:
    """Page Object класс для главной страницы интернет-магазина."""
    
    def __init__(self, driver):
        """
        Инициализация главной страницы.
        
        :param driver: WebDriver экземпляр для управления браузером
        :type driver: WebDriver
        """
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def take_items(self):
        """
        Добавление товаров в корзину.
        
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        self.driver.implicitly_wait(7)

class ScoreItem:
    """Page Object класс для страницы корзины."""
    
    def __init__(self, driver):
        """
        Инициализация страницы корзины.
        
        :param driver: WebDriver экземпляр для управления браузером
        :type driver: WebDriver
        """
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def checkout(self):
        """
        Переход к оформлению заказа.
        
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        self.driver.implicitly_wait(4)

class PostalAndCheck:
    """Page Object класс для страницы оформления заказа."""
    
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.
        
        :param driver: WebDriver экземпляр для управления браузером
        :type driver: WebDriver
        """
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def input_info(self, first_name, last_name, post_code):
        """
        Ввод информации для оформления заказа.
        
        :param first_name: Имя покупателя
        :type first_name: str
        :param last_name: Фамилия покупателя
        :type last_name: str
        :param post_code: Почтовый индекс
        :type post_code: str
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(post_code)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
        self.driver.implicitly_wait(4)

    def get_total_price(self):
        """
        Получение общей суммы заказа.
        
        :return: Текст с общей суммой заказа
        :rtype: str
        """
        result = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        print(result)
        return result