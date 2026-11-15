"""Наскрізний тест: від входу до оформлення замовлення."""
import allure

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.data_generator import random_first_name, random_last_name, random_zip_code

PRODUCT = "Sauce Labs Backpack"


@allure.feature("Покупка товару")
@allure.story("Повний цикл покупки")
@allure.title("Користувач купує товар від входу до фінального повідомлення")
def test_buying_process(driver):
    """Вхід -> додавання товару -> кошик -> Checkout -> доставка -> Finish."""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.get_title_text() == "Products"

    inventory_page.add_product_to_cart(PRODUCT)
    assert inventory_page.get_cart_count() == 1

    inventory_page.open_cart()
    with allure.step("Перевірити, що товар є в кошику"):
        assert PRODUCT in cart_page.get_item_names()

    cart_page.click_checkout()
    checkout_page.fill_shipping_info(random_first_name(), random_last_name(), random_zip_code())
    checkout_page.click_continue()
    checkout_page.click_finish()

    with allure.step("Перевірити фінальне повідомлення"):
        assert checkout_page.get_complete_message() == "Thank you for your order!"
