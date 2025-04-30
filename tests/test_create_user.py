import allure
import pytest


from base_api import BaseApi
from data import gen_user_data


class TestCreateUser:
    @allure.title('Проверка создания уникального пользователя, возврат ответа код 200')
    def test_valid_create_user(self):
        data = gen_user_data()

        response = BaseApi.create_new_user(**data)

        print(f"Request URL: {response.url}")
        print(f"Request Body: {response.request.body}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.json()}")

        assert response.status_code == 200
        assert "accessToken" in response.json()

    @allure.title('Проверка невозможности создания пользователя с существующими данными')
    def test_try_create_user_already_exist(self):
        data = gen_user_data()
        response = BaseApi.create_new_user(**data)
        assert response.status_code == 200
        response_1 = BaseApi.create_new_user(**data)

        print(f"Request URL: {response_1.url}")
        print(f"Request Body: {response_1.request.body}")
        print(f"Response Status Code: {response_1.status_code}")
        print(f"Response Body: {response_1.json()}")

        assert response_1.status_code == 403




