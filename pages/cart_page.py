"""Сторінка кошика Swag Labs."""
import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object сторінки кошика."""

    ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")

    def get_item_names(self):
        """Повертає назви товарів у кошику."""
        return [el.text for el in self.find_all(self.ITEM_NAMES)]

    @allure.step("Користувач натискає кнопку «Checkout»")
    def click_checkout(self):
        """Переходить до оформлення замовлення."""
        self.click(self.CHECKOUT_BUTTON)
