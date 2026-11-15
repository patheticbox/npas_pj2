"""Сторінка каталогу товарів Swag Labs."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object сторінки каталогу."""

    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    SORT_SELECT = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    ITEM_PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")

    # Значення випадного списку сортування
    SORT_NAME_AZ = "az"
    SORT_NAME_ZA = "za"
    SORT_PRICE_LOW_HIGH = "lohi"
    SORT_PRICE_HIGH_LOW = "hilo"

    @staticmethod
    def _add_button(product_name):
        """Будує локатор кнопки «Add to cart» для товару."""
        slug = product_name.lower().replace(" ", "-").replace(".", "").replace("(", "").replace(")", "")
        return (By.ID, f"add-to-cart-{slug}")

    def get_title_text(self):
        """Повертає заголовок сторінки."""
        return self.get_text(self.TITLE)

    @allure.step("Користувач додає товар «{product_name}» до кошика")
    def add_product_to_cart(self, product_name):
        """Додає товар до кошика за назвою."""
        self.click(self._add_button(product_name))

    def get_cart_count(self):
        """Повертає кількість товарів у кошику (число на значку)."""
        return int(self.get_text(self.CART_BADGE))

    @allure.step("Користувач переходить до кошика")
    def open_cart(self):
        """Переходить до кошика."""
        self.click(self.CART_LINK)

    @allure.step("Користувач сортує товари: {option_value}")
    def sort_by(self, option_value):
        """Сортує товари за значенням списку."""
        Select(self.find(self.SORT_SELECT)).select_by_value(option_value)

    def get_product_names(self):
        """Повертає назви товарів у порядку відображення."""
        return [el.text for el in self.find_all(self.ITEM_NAMES)]

    def get_product_prices(self):
        """Повертає ціни товарів у порядку відображення."""
        return [float(el.text.replace("$", "")) for el in self.find_all(self.ITEM_PRICES)]
