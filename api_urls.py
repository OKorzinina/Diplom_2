class APIEndpoints:
    """Конфигурация эндпоинтов API Stellar Burgers"""
    
    BASE_DOMAIN = "stellarburgers.nomoreparties.site"
    BASE_URL = f"https://{BASE_DOMAIN}"
    
    # Аутентификация
    SIGNUP_ENDPOINT = f"{BASE_URL}/api/auth/register"
    SIGNIN_ENDPOINT = f"{BASE_URL}/api/auth/login"
    USER_PROFILE_ENDPOINT = f"{BASE_URL}/api/auth/user"
    
    # Ингредиенты и заказы
    INGREDIENTS_LIST = f"{BASE_URL}/api/ingredients"
    ORDERS_ENDPOINT = f"{BASE_URL}/api/orders"
    
    @classmethod
    def get_full_url(cls, endpoint_name):
        """Возвращает полный URL по имени эндпоинта"""
        endpoints = {
            "register": cls.SIGNUP_ENDPOINT,
            "login": cls.SIGNIN_ENDPOINT,
            "user": cls.USER_PROFILE_ENDPOINT,
            "ingredients": cls.INGREDIENTS_LIST,
            "orders": cls.ORDERS_ENDPOINT
        }
        return endpoints.get(endpoint_name)
