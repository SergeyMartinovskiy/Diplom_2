import allure
import pytest

from data import gen_user_data
from base_api import BaseApi

@allure.title('Создание пользователя. Болванка')
@pytest.fixture(scope='function')
def create_user():
    creating_user_data = gen_user_data()
    BaseApi.create_user(**creating_user_data)

    yield creating_user_data['email'], creating_user_data['password'], creating_user_data['name']

    response = BaseApi.login_user(creating_user_data['email'], creating_user_data['password'])
    BaseApi.delete_user(response.json()['accessToken'])





