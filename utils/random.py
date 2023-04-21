from datetime import datetime
from typing import Tuple

from faker import Faker
from re import match, IGNORECASE

faker = Faker('ru_RU')

class RandomData:
    @staticmethod
    def get_name() -> Tuple[str, str]:
        while True:
            full_name = faker.name()
            name_parts = full_name.split(' ')

            if len(name_parts) < 3:
                continue

            last_name = name_parts[0]
            first_name = name_parts[1]

            if len(first_name) < 2 or len(first_name) > 15:
                continue

            if (match(r'^[а-яё\s]+[a-z]?[а-яё\s]+$', first_name, IGNORECASE) is not None \
                and match(r'^[а-яё]+$', last_name, IGNORECASE) is not None):
                return (first_name, last_name)

    @staticmethod
    def get_phone() -> str:
        while True:
            phone_number = faker.phone_number()

            if len(phone_number) < 11 or len(phone_number) > 13:
                continue

            if match(r'^\+?[0-9]+$', phone_number):
                return phone_number

    @staticmethod
    def get_address() -> str:
        while True:
            address = faker.address()

            if len(address) < 5 or len(address) > 49:
                continue

            if match(r'^[а-яё\s.0-9-,]+$', address, IGNORECASE):
                return address

    @staticmethod
    def get_date_string() -> str:
        date: datetime = faker.date_between(start_date='today', end_date='+1y')
        return date.strftime('%d.%m.%Y')

    @staticmethod
    def get_text() -> str:
        return faker.sentence(nb_words=10)

