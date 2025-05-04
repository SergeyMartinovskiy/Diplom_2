import  allure
import pytest
import conftest
from base_api import BaseApi

from base_api import BaseApi
from data import gen_user_data

class TestLoginUser:
    @allure.title('')

    def test_login_exist_user(self):
        data = gen_user_data()
        response = BaseApi.create_new_user(**data)

        print(f"Request URL: {response.url}")
        print(f"Request Body: {response.request.body}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.json()}")

        assert response.status_code == 200


        response_1 = BaseApi.login_user(email=data['email'], password=data['password'])

        print(f"Request URL: {response_1.url}")
        print(f"Request Body: {response_1.request.body}")
        print(f"Response Status Code: {response_1.status_code}")
        print(f"Response Body: {response_1.json()}")

        assert response_1.status_code == 200
        assert 'accessToken' in response_1.json()

