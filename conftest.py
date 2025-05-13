import allure
import pytest

from data import gen_user_data
from base_api import BaseApi

@allure.title('Создание пользователя. Болванка')
@pytest.fixture(scope='function')
def create_user():
    creating_user_data = gen_user_data()

    response = BaseApi.create_new_user(**creating_user_data)

    assert response.status_code == 200, f'ОШИБКА!!!'

    response_1 = BaseApi.login_user(creating_user_data['email'], creating_user_data['password'])
    assert response_1.status_code == 200
    token = response_1.json().get('accessToken')

    yield {'email':creating_user_data['email'],
           'password':creating_user_data['password'],
           'name':creating_user_data['name'],
           'token': token
           }
    delete_response = BaseApi.delete_user(token)
    assert delete_response.status_code == 202









