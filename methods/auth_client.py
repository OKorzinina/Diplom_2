import requests
import allure
from api_urls import APIEndpoints


class AuthAPIClient:
    """Клиент для работы с API аутентификации"""
    
    @staticmethod
    @allure.step("Создать нового пользователя")
    def create_new_user(user_credentials):
        """Регистрация нового пользователя в системе"""
        return requests.post(
            APIEndpoints.SIGNUP_ENDPOINT,
            json=user_credentials
        )
    
    @staticmethod
    @allure.step("Выполнить вход в систему")
    def authenticate_user(user_email, user_password):
        """Аутентификация существующего пользователя"""
        credentials = {
            "email": user_email,
            "password": user_password
        }
        return requests.post(
            APIEndpoints.SIGNIN_ENDPOINT,
            json=credentials
        )
    
    @staticmethod
    @allure.step("Удалить учетную запись")
    def remove_user_account(auth_token):
        """Удаление пользовательского аккаунта"""
        headers = {"Authorization": auth_token}
        return requests.delete(
            APIEndpoints.USER_PROFILE_ENDPOINT,
            headers=headers
        )
