from faker import Faker
import random
import string

class TestUserFactory:
    """Фабрика для создания тестовых пользователей"""
    
    def __init__(self):
        self.fake = Faker('ru_RU')
    
    def create_valid_user(self):
        """Создать валидного пользователя"""
        first_name = self.fake.first_name()
        last_name = self.fake.last_name()
        
        return {
            "email": f"{first_name.lower()}.{last_name.lower()}@{self.fake.domain_name()}",
            "password": self._generate_secure_password(),
            "name": f"{first_name} {last_name}"
        }
    
    def create_user_without_field(self, excluded_field):
        """Создать пользователя без указанного поля"""
        user = self.create_valid_user()
        if excluded_field in user:
            del user[excluded_field]
        return user
    
    def _generate_secure_password(self, length=12):
        """Сгенерировать безопасный пароль"""
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(chars) for _ in range(length))
