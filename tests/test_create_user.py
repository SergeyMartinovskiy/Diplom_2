import allure
import pytest


from base_api import BaseApi

from conftest import create_user

class TestCreateUser:
    @allure.title('Проверка создания уникального пользователя, возврат ответа код 200')

    def test_valid_create_user(self, create_user):
        email, password, name = create_user

        response = BaseApi.create_user(email=email, password=password, name=name)

        print(f"Request URL: {response.url}")
        print(f"Request Body: {response.request.body}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.json()}")

        assert response.status_code == 200





