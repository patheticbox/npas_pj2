# TechStore / Swag Labs — фреймворк автоматизації тестування

Python, Selenium WebDriver, Pytest, Allure, патерн Page Object.
Об'єкт тестування: https://www.saucedemo.com

## Структура
    pages/            Page Objects (BasePage, LoginPage, InventoryPage, CartPage, CheckoutPage)
    tests/            Тестові сценарії (test_buying_process.py — наскрізний тест)
    utils/            Допоміжні функції (генерація тестових даних)
    reports/          Звіти Allure (у .gitignore)
    conftest.py       Фікстури (драйвер, скріншот при падінні)
    pytest.ini        Конфігурація запуску

## Встановлення залежностей
Потрібні Python 3.10+ і Google Chrome.

    python -m venv venv
    venv\Scripts\activate        # Windows (Linux/macOS: source venv/bin/activate)
    pip install -r requirements.txt

## Запуск тестів
    pytest                       # усі тести
    pytest tests/test_buying_process.py
    set HEADLESS=true            # Windows: запуск без вікна браузера (Linux/macOS: export HEADLESS=true)

Результати Allure зберігаються в `reports/allure-results`.

## Перегляд звіту Allure
Потрібен встановлений Allure Commandline (https://allurereport.org/docs/install/).

    allure serve reports/allure-results

## Запуск у Docker
    docker build -t techstore-tests .
    docker run --rm -v "%cd%/reports:/app/reports" techstore-tests

(Linux/macOS: `-v "$(pwd)/reports:/app/reports"`.) Після запуску: `allure serve reports/allure-results`.

## CI (Jenkins)
Файл `Jenkinsfile` описує етапи: Checkout → Install Dependencies → Lint (flake8) → Run UI Tests (pytest) → Allure Report.
