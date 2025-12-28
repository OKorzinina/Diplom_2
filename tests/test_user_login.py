import pytest
import allure
from methods.auth_client import AuthAPIClient
from test_data import ResponseMessages, TestConstants


@allure.epic("Аутентификация пользователей")
@allure.feature("Вход в систему")
class TestUserAuthentication:
    
    @allure.title("Успешная авторизация с корректными данными")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_valid_user_login(self, temporary_test_user):
        user_credentials = temporary_test_user
        
        with allure.step("Выполнить вход с валидными учетными данными"):
            response = AuthAPIClient.authenticate_user(
                user_credentials["email"],
                user_credentials["password"]
            )
        
        with allure.step("Проверить успешную авторизацию"):
            assert response.status_code == TestConstants.SUCCESS_CODE
            response_data = response.json()
            assert response_data["success"] is True
            assert response_data["user"]["email"] == user_credentials["email"]
            assert "accessToken" in response_data
    
    @allure.title("Попытка входа с неверным email")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_invalid_email(self, temporary_test_user):
        user_credentials = temporary_test_user
        
        with allure.step("Использовать некорректный email"):
            response = AuthAPIClient.authenticate_user(
                TestConstants.INVALID_EMAIL,
                user_credentials["password"]
            )
        
        with allure.step("Проверить ошибку аутентификации"):
            assert response.status_code == TestConstants.UNAUTHORIZED_CODE
            assert response.json() == ResponseMessages.INVALID_CREDENTIALS
    
    @allure.title("Попытка входа с неверным паролем")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_invalid_password(self, temporary_test_user):
        user_credentials = temporary_test_user
        
        with allure.step("Использовать некорректный пароль"):
            response = AuthAPIClient.authenticate_user(
                user_credentials["email"],
                TestConstants.INVALID_PASSWORD
            )
        
        with allure.step("Проверить ошибку аутентификации"):
            assert response.status_code == TestConstants.UNAUTHORIZED_CODE
            assert response.json() == ResponseMessages.INVALID_CREDENTIALS
