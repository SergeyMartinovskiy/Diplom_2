import allure
import pytest

from data import gen_user_data
from base_api import BaseApi

@allure.title('Создание пользователя. Болванка')
@pytest.fixture(scope='function')
def create_user():
    creating_user_data = gen_user_data()

    response = BaseApi.create_user(**creating_user_data)

    assert response.status_code == 200, f'ОШИБКА!!!'

    response_1 = BaseApi.login_user(creating_user_data['email'], creating_user_data['password'])
    assert response_1.status_code == 200
    token = response_1.json().get('accessToken')

    yield creating_user_data['email'], creating_user_data['password'], creating_user_data['name']

    delete_response = BaseApi.delete_user(token)
    assert delete_response.status_code == 200






