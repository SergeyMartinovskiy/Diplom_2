from faker import Faker
import random
from random import sample

faker = Faker()

def gen_fake_email():
    base_email = f'tester{random.randint(1,10000)}'
    email = faker.email()
    return f'{base_email}_{email}'

def gen_fake_password(lenght=8):
    password = faker.password(length=lenght)
    return password.lower()

def gen_fake_firstname(max_lenght=8):
    while True:
        name = faker.first_name()
        if len(name) <= max_lenght:
            return name.capitalize()

def gen_user_data():
    return {
            'email': gen_fake_email(),
            'password': gen_fake_password(),
            'name': gen_fake_firstname()
           }

def generator_data_of_order(ingredients, max_ingredients = 4):
    available_ids = [ing['_id'] for ing in ingredients if '_id' in ing]
    count = min (max_ingredients, len(available_ids))
    return sample (available_ids, count)


