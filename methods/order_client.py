import requests
import allure
from api_urls import APIEndpoints


class OrderAPIClient:
    """Клиент для работы с API заказов"""
    
    @staticmethod
    @allure.step("Сформировать новый заказ")
    def place_new_order(ingredient_ids, auth_token=None):
        """
        Создание нового заказа
        
        Args:
            ingredient_ids: список ID ингредиентов
            auth_token: токен авторизации 
        """
        request_headers = {}
        
        if auth_token:
            # Нормализуем токен (убираем 'Bearer ' если есть)
            normalized_token = auth_token.replace("Bearer ", "")
            request_headers["Authorization"] = f"Bearer {normalized_token}"
        
        order_data = {"ingredients": ingredient_ids}
        
        return requests.post(
            APIEndpoints.ORDERS_ENDPOINT,
            json=order_data,
            headers=request_headers
        )
