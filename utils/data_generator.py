"""Генерація тестових даних."""
import random
import string


def random_string(length=8):
    """Повертає випадковий рядок з малих латинських літер."""
    return "".join(random.choices(string.ascii_lowercase, k=length))


def random_email(domain="example.com"):
    """Повертає випадкову електронну адресу."""
    return f"{random_string(10)}@{domain}"


def random_first_name():
    """Повертає випадкове ім'я (з великої літери)."""
    return random_string(6).capitalize()


def random_last_name():
    """Повертає випадкове прізвище (з великої літери)."""
    return random_string(8).capitalize()


def random_zip_code():
    """Повертає випадковий п'ятицифровий поштовий індекс."""
    return "".join(random.choices(string.digits, k=5))
