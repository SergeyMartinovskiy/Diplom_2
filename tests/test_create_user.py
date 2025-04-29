import allure
import requests
from data import gen_fake_password, gen_fake_email, gen_fake_firstname
from urls import URLS
from conftest import create_user

class TestCreateUser:
    @allure.title('Проверка создания уникального пользователя, возврат ответа код 201 и тело ответа ok:true')
    def test_valid_create_user(self, create_user):
        create_user_request = create_user

        assert create_user_request.json() == {
            'success': True,
            'user': {
                'email': '',
                'name': ''
                    },
            'accessToken': "Bearer   ",
            'refreshToken': ''
            }



