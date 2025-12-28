import pytest
import allure
from methods.order_client import OrderAPIClient
from api_helpers import extract_auth_token
from test_data import ResponseMessages, TestConstants


@allure.epic("Управление заказами")
@allure.feature("Создание заказов")
class TestOrderProcessing:

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_order_with_auth_and_ingredients(self, temporary_test_user, fetch_available_ingredients):
        user_data = temporary_test_user
        ingredients = fetch_available_ingredients

        with allure.step("Получить токен авторизации"):
            auth_token = extract_auth_token(user_data)

        with allure.step("Создать заказ с ингредиентами"):
            response = OrderAPIClient.place_new_order(ingredients, auth_token)

        with allure.step("Проверить успешное создание заказа"):
            assert response.status_code == TestConstants.SUCCESS_CODE
            response_data = response.json()
            assert response_data["success"] is True
            assert "order" in response_data
            assert "number" in response_data["order"]

    @allure.title("Создание заказа без ингредиентов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_without_ingredients(self, temporary_test_user):
        user_data = temporary_test_user

        with allure.step("Получить токен авторизации"):
            auth_token = extract_auth_token(user_data)

        with allure.step("Создать заказ с пустым списком ингредиентов"):
            response = OrderAPIClient.place_new_order([], auth_token)

        with allure.step("Проверить валидацию ингредиентов"):
            assert response.status_code == TestConstants.BAD_REQUEST_CODE
            assert response.json() == ResponseMessages.INGREDIENTS_REQUIRED

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    @allure.severity(allure.severity_level.MINOR)
    def test_order_with_invalid_ingredient_hash(self, temporary_test_user):
        user_data = temporary_test_user

        with allure.step("Получить токен авторизации"):
            auth_token = extract_auth_token(user_data)

        with allure.step("Использовать невалидные ID ингредиентов"):
            invalid_ingredients = [TestConstants.BAD_INGREDIENT_ID]
            response = OrderAPIClient.place_new_order(invalid_ingredients, auth_token)

        with allure.step("Проверить ошибку сервера"):
            # Сервер может вернуть 500 или другую ошибку
            assert response.status_code == TestConstants.SERVER_ERROR_CODE

    @allure.title("Создание заказа без авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_without_authentication(self, fetch_available_ingredients):
        ingredients = fetch_available_ingredients

        with allure.step("Создать заказ без токена авторизации"):
            response = OrderAPIClient.place_new_order(ingredients)

        with allure.step("Проверить код ответа и тело ошибки"):
            # Ожидаем ошибку авторизации, как того требует документация
            assert response.status_code == TestConstants.UNAUTHORIZED_CODE
            # Проверяем сообщение об ошибке
            assert response.json() == ResponseMessages.AUTH_REQUIRED


