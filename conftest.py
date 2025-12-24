import pytest
import requests
from user_generator import TestUserFactory
from methods.auth_client import AuthAPIClient
from api_urls import APIEndpoints


@pytest.fixture
def user_factory():
    """Фабрика для создания тестовых пользователей"""
    return TestUserFactory()


@pytest.fixture(scope="function")
def temporary_test_user():
    """Создать и удалить тестового пользователя"""
    factory = TestUserFactory()
    test_user = factory.create_valid_user()
    
    auth_client = AuthAPIClient()
    registration_result = auth_client.create_new_user(test_user)
    
    if registration_result.status_code != 200:
        pytest.skip(f"Не удалось создать пользователя: {registration_result.text}")
    
    yield test_user
    
    # Очистка после теста
    auth_response = auth_client.authenticate_user(
        test_user["email"], 
        test_user["password"]
    )
    
    if auth_response.status_code == 200:
        auth_token = auth_response.json().get("accessToken")
        auth_client.remove_user_account(auth_token)


@pytest.fixture(scope="function")
def user_data_cleaner():
    """Фикстура для очистки пользовательских данных"""
    user_info = {}
    
    yield user_info
    
    if user_info.get("email") and user_info.get("password"):
        auth_client = AuthAPIClient()
        auth_response = auth_client.authenticate_user(
            user_info["email"], 
            user_info["password"]
        )
        
        if auth_response.status_code == 200:
            auth_token = auth_response.json().get("accessToken")
            auth_client.remove_user_account(auth_token)


@pytest.fixture(scope="session")
def fetch_available_ingredients():
    """Получить список доступных ингредиентов"""
    ingredients_url = APIEndpoints.INGREDIENTS_LIST
    api_response = requests.get(ingredients_url)
    
    if api_response.status_code != 200:
        pytest.fail(f"Не удалось получить ингредиенты: {api_response.text}")
    
    response_data = api_response.json()
    if not response_data.get("success"):
        pytest.fail("API не вернуло успешный ответ")
    
    # Возвращаем первые 2 ID ингредиентов для тестов
    return [item["_id"] for item in response_data.get("data", [])[:2]]
