import  allure
import pytest

from base_api import BaseApi

class TestMakeOrder:
    @allure.title('Проверка успешного создания заказа с авторизацией')
    def test_make_order_with_authorisation(self):
