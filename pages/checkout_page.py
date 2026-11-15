"""Сторінки оформлення замовлення Swag Labs."""
import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page Object кроків оформлення замовлення."""

    FIRST_NAME = (By.CSS_SELECTOR, "[data-test='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "[data-test='lastName']")
    POSTAL_CODE = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")
    FINISH_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    @allure.step("Користувач заповнює форму доставки: {first_name} {last_name}, {postal_code}")
    def fill_shipping_info(self, first_name, last_name, postal_code):
        """Заповнює форму доставки."""
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.POSTAL_CODE, postal_code)

    @allure.step("Користувач натискає кнопку «Continue»")
    def click_continue(self):
        """Переходить до огляду замовлення."""
        self.click(self.CONTINUE_BUTTON)

    @allure.step("Користувач натискає кнопку «Finish»")
    def click_finish(self):
        """Завершує замовлення."""
        self.click(self.FINISH_BUTTON)

    def get_complete_message(self):
        """Повертає фінальне повідомлення."""
        return self.get_text(self.COMPLETE_HEADER)

    def get_error_text(self):
        """Повертає текст помилки форми."""
        return self.get_text(self.ERROR_MESSAGE)
