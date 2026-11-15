"""Тести каталогу товарів."""
import allure
import pytest

from pages.inventory_page import InventoryPage


@allure.feature("Каталог товарів")
@allure.title("Сортування за ціною: {option}")
@pytest.mark.parametrize("option, reverse", [
    (InventoryPage.SORT_PRICE_LOW_HIGH, False),
    (InventoryPage.SORT_PRICE_HIGH_LOW, True),
])
@pytest.mark.usefixtures("logged_in_driver")
def test_sort_by_price(inventory_page, option, reverse):
    """Ціни відображаються у відсортованому порядку."""
    inventory_page.sort_by(option)
    prices = inventory_page.get_product_prices()
    assert prices == sorted(prices, reverse=reverse)
