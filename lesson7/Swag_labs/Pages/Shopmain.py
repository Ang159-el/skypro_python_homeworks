from selenium.webdriver.common.by import By
from lesson7.constants import Online_store_URL

class ShopmainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(Online_store_URL)

 # Заполняем поля
    def registration_fields(self):
        self._name = (By.ID, "user-name")
        self._pass = (By.ID, "password")
        self._log_button = (By.ID, "login-button")
        self.browser.find_element(*self._name).send_keys("standart_user")
        self.browser.find_element(*self._pass).send_keys("secret_sauce")
        self.browser.find_element(*self._log_button).click()

 # Ищем кнопкидобавления товара в корзину
    def buy_issue(self):
        self.Sauce_Labs_Backpack = (By.ID, "add-to-cart-saauce-labs-backpack")
        self.Sauce_Bolt_TShirt = (By.ID, "add-to-cart-saauce-labs-bolt-t-shirt")
        self.Sauce_Labs_Onesie= (By.ID, "add-to-cart-saauce-labs-onesie")

 # Добавляем товары в корзину
    def click_issue(self):
        self.browser.find_element(*self.Sauce_Labs_Backpack).click()
        self.browser.find_element(*self.Sauce_Bolt_TShirt).click()
        self.browser.find_element(*self.Sauce_Labs_Onesie).click()
        
 # Переходим в корзину и оформляем заказ
    def into_container(self)
        self.Container = (By.ID, "shopping_cart_container")
        self.browser.find_element(*self.Container).click()
        