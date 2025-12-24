import pytest
import allure
from user_generator import TestUserFactory
from methods.auth_client import AuthAPIClient
from test_data import ResponseMessages, TestConstants


@allure.epic("Регистрация пользователей")
@allure.feature("Создание учетной записи")
class TestUserRegistration:
    
    @allure.title("Успешная регистрация нового пользователя")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_successful_user_registration(self, user_data_cleaner):
        factory = TestUserFactory()
        new_user = factory.create_valid_user()
        user_data_cleaner.update(new_user)
        
        with allure.step("Отправить запрос на регистрацию"):
            response = AuthAPIClient.create_new_user(new_user)
        
        with allure.step("Проверить успешность регистрации"):
            assert response.status_code == TestConstants.SUCCESS_CODE
            response_data = response.json()
            assert response_data["success"] is True
            assert response_data["user"]["email"] == new_user["email"]
            assert "accessToken" in response_data
    
    @allure.title("Попытка регистрации уже существующего пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_duplicate_user_registration(self, temporary_test_user):
        existing_user = temporary_test_user
        
        with allure.step("Повторно зарегистрировать того же пользователя"):
            response = AuthAPIClient.create_new_user(existing_user)
        
        with allure.step("Проверить сообщение о дубликате"):
            assert response.status_code == TestConstants.FORBIDDEN_CODE
            assert response.json() == ResponseMessages.DUPLICATE_USER
    
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    @allure.title("Регистрация без обязательного поля: {missing_field}")
    @allure.severity(allure.severity_level.NORMAL)
    def test_registration_with_missing_field(self, missing_field):
        factory = TestUserFactory()
        incomplete_user = factory.create_user_without_field(missing_field)
        
        with allure.step(f"Отправить запрос без поля '{missing_field}'"):
            response = AuthAPIClient.create_new_user(incomplete_user)
        
        with allure.step("Проверить валидацию обязательных полей"):
            assert response.status_code == TestConstants.FORBIDDEN_CODE
            assert response.json() == ResponseMessages.REQUIRED_FIELDS_MISSING
