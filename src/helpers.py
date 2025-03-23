import random

def generate_registration_user():
    names = ['alina', 'ivan', 'mariya', 'katya', 'jake', 'anya']
    name = random.choice(names)

    letters = 'abcdefghijklmnopkrstuvwxyz'
    digits = '0123456789'
    username = ''.join(random.choices(letters + digits))
    domains = ['yandex.ru', 'mail.ru', 'gmail.com']
    email = f'{username}@{random.choices(domains)}'

    password = ''.join(random.choices(letters + digits, k = 6))

    return {
        'name': name,
        'email': email,
        'password': password
    }

test_user = generate_registration_user()