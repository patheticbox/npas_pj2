"""Тести входу в систему."""
import allure
import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.feature("Авторизація")
@allure.title("Успішний вхід стандартним користувачем")
def test_successful_login(driver):
    """Вхід із валідними даними відкриває каталог."""
    LoginPage(driver).open().login("standard_user", "secret_sauce")
    assert InventoryPage(driver).get_title_text() == "Products"


@allure.feature("Авторизація")
@allure.title("Помилка входу з неправильними даними: {username}")
@pytest.mark.parametrize("username, password, expected", [
    ("standard_user", "wrong_pass",
     "Epic sadface: Username and password do not match any user in this service"),
    ("locked_out_user", "secret_sauce",
     "Epic sadface: Sorry, this user has been locked out."),
])
def test_login_errors(driver, username, password, expected):
    """Некоректні дані показують повідомлення про помилку."""
    login_page = LoginPage(driver).open()
    login_page.login(username, password)
    assert login_page.get_error_text() == expected
