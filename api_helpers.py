from methods.auth_client import AuthAPIClient


def extract_auth_token(credentials):
    """Извлечь токен авторизации по учетным данным"""
    auth_client = AuthAPIClient()
    auth_response = auth_client.authenticate_user(
        credentials["email"], 
        credentials["password"]
    )
    
    if auth_response.status_code == 200:
        return auth_response.json().get("accessToken")
    
    raise ValueError(f"Не удалось получить токен: {auth_response.text}")
