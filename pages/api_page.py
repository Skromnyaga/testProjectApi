import allure
import requests
from generators.user_generator import generate_person
from pydantic.error_wrappers import ValidationError

class APIPage:
    def __init__(self, response):
        self.response = response
        # self.response_json = response.json()
        # self.response_status = response.status_code
        # self.parsed_object = None

    @allure.step("Add new user")
    def add_new_information(self, data):
        url = f"{self.response}/api/users"
        response = requests.post(url, json=data)
        return response

    @allure.step("Generate person")
    def generate_json_person(self):
        person = next(generate_person())
        user_data = {
            "name": person.name,
            "job": person.job
        }
        return user_data

    @allure.step("Login")
    def login(self, login, password):
        url = f"{self.response}/api/login"
        data = {
            "email": login,
            "password": password
        }
        response = requests.post(url, json=data)
        return response


    # def validate(self, schema):
    #     try:
    #         if isinstance(self.response_json, list):
    #             for item in self.response_json:
    #                 parsed_object = schema.parse_obj(item)
    #                 self.parsed_object = parsed_object
    #         else:
    #             schema.parse_obj(self.response_json)
    #     except ValidationError:
    #         raise AssertionError(
    #             "Could not map received object to pydantic schema"
    #         )