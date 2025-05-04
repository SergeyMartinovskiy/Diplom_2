import allure
import requests
from urls import URLS


class BaseApi:

    @staticmethod
    @allure.title('Создание пользователя')
    def create_new_user(email, password, name):
        data = {'email': email,
                "password":password,
                'name': name}
        return requests.post(URLS.URL_CREATE_USERS, json=data)

    @staticmethod
    @allure.title('Регистрация пользователя')
    def login_user(email, password):
        data = {'email': email,
                "password":password
                }
        return requests.post(URLS.URL_LOGIN_USERS, json=data)

    @staticmethod
    @allure.title('Удаление пользователя')
    def delete_user(token):
        headers = {'Authorization': token}
        return requests.delete(URLS.URL_DELETE_USERS, headers=headers)

    @staticmethod
    @allure.title('Изменение данных пользователя')
    def change_date_user(token, **data):
        headers = {'Authorization': token}
        return requests.patch(URLS.URL_UPDATE_USERS, json=data, headers=headers)

    @staticmethod
    @allure.title('Создание заказа')
    def make_order(token, ingredients):
        data = {'ingredients': ingredients}
        headers = {'Authorization': token}
        return requests.post(URLS.URL_CREATE_ORDER, json = data, headers=headers)

    @staticmethod
    @allure.title('Получение списка заказов')
    def get_ingredients():
        return requests.get(URLS.URL_GET_INGREDIENTS)
