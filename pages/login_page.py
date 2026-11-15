"""Сторінка входу Swag Labs."""
import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object сторінки входу."""

    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    @allure.step("Користувач відкриває сторінку входу")
    def open(self):
        """Відкриває сторінку входу."""
        self.open_url(self.URL)
        return self

    @allure.step("Користувач вводить логін «{username}» і пароль")
    def enter_credentials(self, username, password):
        """Вводить логін і пароль."""
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)

    @allure.step("Користувач натискає кнопку «Login»")
    def click_login(self):
        """Натискає кнопку входу."""
        self.click(self.LOGIN_BUTTON)

    @allure.step("Користувач входить у систему як «{username}»")
    def login(self, username, password):
        """Виконує повний вхід."""
        self.enter_credentials(username, password)
        self.click_login()

    def get_error_text(self):
        """Повертає текст повідомлення про помилку."""
        return self.get_text(self.ERROR_MESSAGE)
