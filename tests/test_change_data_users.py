import  allure
import pytest

from base_api import BaseApi
from data import gen_user_data, gen_fake_email

class TestChangeDataUser:
    @allure.title('Проверка невозможности изменения данных неавторизованного пользователя ')
    def test_change_data_unuthorised_user(self):
        data = gen_user_data()
        BaseApi.create_new_user(**data)
        update_data = {
            'name':'New name',
            'email': 'New_email@ser.com',
            'password': 'new_password'
        }
        response_update = BaseApi.change_date_user(token=None, **update_data)
        assert response_update.status_code == 401
        assert 'You should be authorised' in response_update.json().get('message')

    @allure.title('Проверка успешного обновления данных пользователя')
    @pytest.mark.parametrize('update_type',
                             ['email', 'name', 'both'])
    def test_succesfull_change_data_user(self, update_type):
        data = gen_user_data()
        BaseApi.create_new_user(**data)
        response_1 = BaseApi.login_user(email=data['email'], password=data['password'])
        token = response_1.json()['accessToken']

        update_data = {}
        if update_type in ['email', 'both']:
            update_data['email'] = gen_fake_email()
        if update_type in ['name', 'both']:
            update_data['name'] = 'NewSerg'

        response_update = BaseApi.change_date_user(token, **update_data)
        assert response_update.status_code == 200
        delete_response = BaseApi.delete_user(token)
        assert delete_response.status_code == 202



