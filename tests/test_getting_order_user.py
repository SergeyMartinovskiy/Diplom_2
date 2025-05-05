import allure
import pytest
from base_api import BaseApi
from data import gen_user_data

class TestGettingOrderUser:

    @allure.title('Получение заказов авторизованного пользователя')
    def test_getting_order_authorised_user(self):
        data = gen_user_data()
        response = BaseApi.create_new_user(**data)
        BaseApi.login_user(email=data['email'], password=data['password'])
        token = response.json().get('accessToken')
        response_2 = BaseApi.getting_orders_user(token)
        assert response_2.status_code == 200
        assert response_2.json()['success'] is True

        delete_response = BaseApi.delete_user(token)
        assert delete_response.status_code == 202

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_getting_order_unauthorised_user(self):
        response = BaseApi.getting_orders_user('')
        assert response.status_code == 401
        assert 'You should be authorised' in response.json().get('message')



