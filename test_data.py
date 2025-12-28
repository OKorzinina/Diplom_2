class ResponseMessages:
    """Сообщения об ошибках API"""
    
    DUPLICATE_USER = {
        "success": False,
        "message": "User already exists"
    }
    
    REQUIRED_FIELDS_MISSING = {
        "success": False,
        "message": "Email, password and name are required fields"
    }
    
    INVALID_CREDENTIALS = {
        "success": False,
        "message": "email or password are incorrect"
    }
    
    AUTH_REQUIRED = {
        "success": False,
        "message": "You should be authorised"
    }
    
    INGREDIENTS_REQUIRED = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }


class TestConstants:
    """Константы для тестирования"""
    
    # Тестовые учетные данные
    INVALID_EMAIL = "nonexistent.user@testdomain.example"
    INVALID_PASSWORD = "wrong_password_12345"
    
    # Неверные данные
    BAD_INGREDIENT_ID = "invalid_id_12345_67890"
    
    # Коды статусов
    SUCCESS_CODE = 200
    BAD_REQUEST_CODE = 400
    UNAUTHORIZED_CODE = 401
    FORBIDDEN_CODE = 403
    SERVER_ERROR_CODE = 500
