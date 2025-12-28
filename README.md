# Диплом #
## Задание 2: Автотесты для API сервиса Stellar Burgers (https://stellarburgers.education-services.ru) ##

## Структура проекта
- `methods/` - Клиенты для работы с API
- `tests/` - Тестовые сценарии
- `conftest.py` - Фикстуры pytest
- `test_data.py` - Тестовые данные
- `api_urls.py` - URL endpoints
- `user_generator.py` - Генератор тестовых пользователей

### Запуск тестов

* Установить зависимости:
pip install -r requirements.txt

* Запустить тесты:
pytest tests/ --alluredir=allure-results

* Создать отчет Allure:
allure serve allure-results

### Тестовые сценарии
* регистрация пользователя
* авторизация пользователя
* создание заказов
