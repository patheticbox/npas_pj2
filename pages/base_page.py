"""Базовий клас сторінки з обгортками над методами Selenium."""
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DEFAULT_TIMEOUT = 10


class BasePage:
    """Спільні методи для всіх Page Object класів (явні очікування)."""

    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Відкрити адресу {url}")
    def open_url(self, url):
        """Відкриває сторінку за адресою."""
        self.driver.get(url)

    def find(self, locator):
        """Знаходить елемент, очікуючи його появи та видимості."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        """Знаходить усі елементи, очікуючи появи хоча б одного."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """Натискає елемент після очікування його клікабельності."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        """Очищає поле та вводить текст."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Повертає текст елемента."""
        return self.find(locator).text

    def get_current_url(self):
        """Повертає поточну адресу."""
        return self.driver.current_url

    def wait_for_url_contains(self, fragment):
        """Очікує, поки адреса міститиме фрагмент."""
        return self.wait.until(EC.url_contains(fragment))
