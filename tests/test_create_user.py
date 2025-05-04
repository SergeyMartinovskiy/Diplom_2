import allure
import pytest

from base_api import BaseApi
from data import gen_user_data

# принты оставил для понимания выводов и отслеживания значений

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

        token = response.json().get('accessToken')
        delete_response = BaseApi.delete_user(token)
        assert delete_response.status_code == 202


    @allure.title('Проверка невозможности создания пользователя с существующими данными')
    def test_try_create_user_already_exist(self):
        data = gen_user_data()
        response = BaseApi.create_new_user(**data)

        print(f"Request URL: {response.url}")
        print(f"Request Body: {response.request.body}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.json()}")

        assert response.status_code == 200
        response_1 = BaseApi.create_new_user(**data)

        print(f"Request URL: {response_1.url}")
        print(f"Request Body: {response_1.request.body}")
        print(f"Response Status Code: {response_1.status_code}")
        print(f"Response Body: {response_1.json()}")

        assert response_1.status_code == 403
        assert 'User already exists' in response_1.json().get('message')



    @allure.title('Проверка получения ошибки 403 при создании пользователя с незаполненным одним из полей')
    @pytest.mark.parametrize('empty_necessary_field', ["email", 'password', 'name'])
    def test_try_create_user_with_empty_necessary_field(self, empty_necessary_field):
        data = gen_user_data()
        data[empty_necessary_field] = ''

        response = BaseApi.create_new_user(**data)

        print(f"Request URL: {response.url}")
        print(f"Request Body: {response.request.body}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.json()}")

        assert response.status_code == 403
        assert 'Email, password and name are required fields' in response.json().get('message')




