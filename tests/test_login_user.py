import  allure
import pytest

from base_api import BaseApi
from data import gen_user_data

class TestLoginUser:

    @allure.title('Проверка авторизации с неправильным email')
    def test_login_user_with_wrong_email(self, create_user):
        data = create_user
        wrong_email = 'wrong_email@ser.com'
        correct_password = data['password']

        response_1 = BaseApi.login_user(email=wrong_email, password=correct_password)

        assert response_1.status_code == 401
        assert 'email or password are incorrect' in response_1.json().get('message')

    @allure.title('Проверка авторизации с неправильным паролем')
    def test_login_user_with_wrong_password(self, create_user):
        data = create_user
        correct_email = data['email']
        wrong_password = 'wrong_password'

        response_1 = BaseApi.login_user(email=correct_email, password=wrong_password)

        assert response_1.status_code == 401
        assert 'email or password are incorrect' in response_1.json().get('message')

    @allure.title('Проверка авторизации с неправильным email и паролем')
    def test_login_user_with_both_wrong_credentials(self, create_user):
        data = create_user

        wrong_email = 'wrong_email@ser.com'
        wrong_password = 'wrong_password'

        response_1 = BaseApi.login_user(email=wrong_email, password=wrong_password)

        assert response_1.status_code == 401
        assert 'email or password are incorrect' in response_1.json().get('message')

    @allure.title('Проверка авторизации пользователя с действующими логином и паролем')
    def test_login_exist_user(self, create_user):
        user_data = create_user
        response_1 = BaseApi.login_user(email=user_data['email'], password=user_data['password'])
        assert response_1.status_code == 200
        assert 'accessToken' in response_1.json()


