import  allure
import pytest

from base_api import BaseApi
from data import generator_data_of_order
from data import gen_user_data


class TestMakeOrder:
    @allure.title('Проверка успешного создания заказа с авторизацией')
    def test_make_order_with_authorisation(self):
        data = gen_user_data()
        response = BaseApi.create_new_user(**data)
        BaseApi.login_user(email=data['email'], password=data['password'])

        token = response.json().get('accessToken')

        ingredients_response = BaseApi.get_ingredients()
        available_ingredients = ingredients_response.json()['data']
        order_ingredients = generator_data_of_order(available_ingredients)

        response_2 = BaseApi.make_order(token = token, ingredients = order_ingredients)
        assert response_2.status_code == 200
        assert response_2.json()['success'] is True

    @allure.title('Проверка невозможности создания заказа без авторизации')
    @allure.description('Зафиксирован баг.'
                        'ОР: неавторизованный пользователь не может создать заказ. Код ответа 401'
                        'ФР: неавторизованный пользователь может создать заказ. Код ответа 200')
    def test_make_order_without_authorisation(self):
        ingredients_response = BaseApi.get_ingredients()
        available_ingredients = ingredients_response.json()['data']
        order_ingredients = generator_data_of_order(available_ingredients)

        response_2 = BaseApi.make_order(token = '', ingredients = order_ingredients)
        assert response_2.status_code == 400
        assert response_2.json()['success'] is False

    @allure.title('Проверка возможности создания заказа без ингридиентов')
    def test_make_order_without_ingredients(self):
        data = gen_user_data()
        response = BaseApi.create_new_user(**data)
        BaseApi.login_user(email=data['email'], password=data['password'])

        token = response.json().get('accessToken')

        response_2 = BaseApi.make_order(token=token, ingredients='')
        assert response_2.status_code == 400
        assert 'Ingredient ids must be provided' in response_2.json().get('message')









