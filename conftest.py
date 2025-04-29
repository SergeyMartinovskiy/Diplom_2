import allure
import requests
from allure_commons import fixture

from urls import URLS
from data import gen_fake_password, gen_fake_firstname, gen_fake_email
import pytest

@allure.title('Создание пользователя. Болванка')
@pytest.fixture(scope='function')
def create_user():
    payload = {
        'email': gen_fake_email(),
        'password': gen_fake_password(),
        'name': gen_fake_firstname()
    }
    response = requests.post(URLS.URL_CREATE_USERS, data = payload)

    yield response

