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
    yield creating_user_data['email'], creating_user_data['password'], creating_user_data['name']

    response_1 = BaseApi.login_user(creating_user_data['email'], creating_user_data['password'])
    if response_1.status_code == 200:
        BaseApi.delete_user(response.json()['accessToken'])





