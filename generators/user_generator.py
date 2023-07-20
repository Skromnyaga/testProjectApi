from schemas.user import User
from faker import Faker

faker_en = Faker('En')
Faker.seed()

def generate_person():
    yield User(
        name=faker_en.first_name(),
        job=faker_en.job()
    )