import allure
import pytest

from base_api import BaseApi
from data import gen_user_data


class TestCreateUser:
    @allure.title('Проверка создания уникального пользователя, возврат ответа код 200')
    def test_valid_create_user(self):
        data = gen_user_data()
        response = BaseApi.create_new_user(**data)
        assert response.status_code == 200
        assert 'accessToken' in response.json()

    @allure.title('Проверка невозможности создания пользователя с существующими данными')
    def test_try_create_user_already_exist(self, create_user):
        existing_user_data = create_user

        response_1 = BaseApi.create_new_user(
            email=existing_user_data['email'],
            password=existing_user_data['password'],
            name=existing_user_data['name'])

        assert response_1.status_code == 403, 'Должен быть код ошибки 403!'
        assert 'User already exists' in response_1.json().get('message')


    @allure.title('Проверка получения ошибки 403 при создании пользователя с незаполненным одним из полей')
    @pytest.mark.parametrize('empty_necessary_field', ["email", 'password', 'name'])
    def test_try_create_user_with_empty_necessary_field(self, empty_necessary_field):
        data = gen_user_data()
        data[empty_necessary_field] = ''
        response = BaseApi.create_new_user(**data)

        assert response.status_code == 403
        assert 'Email, password and name are required fields' in response.json().get('message')






