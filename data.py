from faker import Faker

faker = Faker()

def gen_fake_email(locale="ru_RU"):
    email = faker.email
    return email[:locale]

def gen_fake_password(lenght=8):
    password = faker.password
    return password[:lenght]

def gen_fake_name(lenght=8):
    name = faker.name
    return name[:lenght]

