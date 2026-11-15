"""Fixture Manager: керування драйвером і скріншотами."""
# pylint: disable=redefined-outer-name
import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

STANDARD_USER = "standard_user"
PASSWORD = "secret_sauce"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):  # pylint: disable=unused-argument
    """Зберігає результат фази тесту, щоб фікстура знала про падіння."""
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(scope="function")
def driver(request):
    """Створює Chrome перед тестом, додає скріншот при падінні та закриває браузер."""
    options = Options()
    if os.getenv("HEADLESS", "").lower() == "true":
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    yield browser
    report = getattr(request.node, "rep_call", None)
    if report is not None and report.failed:
        allure.attach(browser.get_screenshot_as_png(), name="Скріншот при падінні",
                      attachment_type=allure.attachment_type.PNG)
    browser.quit()


@pytest.fixture
def login_page(driver):
    """Page Object сторінки входу."""
    return LoginPage(driver)


@pytest.fixture
def inventory_page(driver):
    """Page Object каталогу."""
    return InventoryPage(driver)


@pytest.fixture
def logged_in_driver(driver, login_page):
    """Драйвер із виконаним входом standard_user."""
    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)
    return driver
