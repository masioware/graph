from faker import Faker


def generate_people(number):
    for _ in range(number):
        yield {
            "name": Faker("pt_BR").name(),
            "birth": Faker("pt_BR").date_of_birth()
        }
