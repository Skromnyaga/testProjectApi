import allure

from pages.api_page import APIPage
from dotenv import load_dotenv
import os


class TestAPI:
    def setup_class(self):
        load_dotenv()
        api_url = os.getenv("API_URL")
        self.login = os.getenv("LOGIN")
        self.password = os.getenv("PASSWORD")
        self.api = APIPage(api_url)


    @allure.story("Add new information")
    def test_add_new_info(self):
        data = self.api.generate_json_person()
        response = self.api.add_new_information(data)
        assert response.status_code == 201


    @allure.story("Successful login")
    def test_successful_login(self):
        response = self.api.login(self.login, self.password)
        assert response.status_code == 200


    @allure.story("Login without password")
    def test_login_without_password(self):
        response = self.api.login(self.login, self.password)
        assert response.status_code == 200
