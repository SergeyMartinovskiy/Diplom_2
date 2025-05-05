import  allure
import pytest

from base_api import BaseApi
from data import gen_user_data

class TestLoginUser:
    @allure.title('Проверка авторизации пользователя с действующими логином и паролем')
    def test_login_exist_user(self):
        data = gen_user_data()
        response = BaseApi.create_new_user(**data)
        assert response.status_code == 200

        response_1 = BaseApi.login_user(email=data['email'], password=data['password'])
        assert response_1.status_code == 200
        assert 'accessToken' in response_1.json()

        token = response.json().get('accessToken')
        delete_response = BaseApi.delete_user(token)
        assert delete_response.status_code == 202

    @allure.title('Проверка авторизации пользователя с неверными логином или паролем')
    @pytest.mark.parametrize('email, password',
                             [('wrong_email@ser.com', 'correct_password'),
                              ('correct_email', 'wrong_password'),
                              ('wrong_email@ser.com', 'wrong_password')])
    def test_login_user_with_wrong_login_or_password(self, email, password):
        data = gen_user_data()
        BaseApi.create_new_user(**data)

        correct_email = data['email']
        correct_password = data['password']

        test_email = correct_email if email == "correct_email" else email
        test_password = correct_password if password == 'correct_password' else password

        response_1 = BaseApi.login_user(email=test_email, password=test_password)

        assert response_1.status_code == 401
        assert 'email or password are incorrect' in response_1.json().get('message')







