import  allure
import pytest
import conftest
from base_api import BaseApi

from base_api import BaseApi
from data import gen_user_data

class TestChangeDataUser:
    @allure.title('Проверка изменения данных неавторизованного пользователя ')
    def test_change_data_unuthorised_user(self):
        data = gen_user_data()
        response = BaseApi.create_new_user(**data)
        assert response.status_code == 200

        update_data = {
            'name':'New name',
            'email': 'New_email@ser.com',
            'password': 'new_password'
        }

        response_update = BaseApi.change_date_user(token=None, **update_data)
        assert response_update.status_code == 401
        assert 'You should be authorised' in response_update.json().get('message')

