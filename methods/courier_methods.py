import requests
from urls import TotalUrl
import allure


class CourierMeth:
    @allure.step("Логин курьера")
    def login_courier(self, login, password):
        payload = {"login": login, "password": password}
        respons = requests.post(TotalUrl.LOGIN_IN_THE_SYSTEM_URL, data=payload)
        return respons.status_code, respons.json()

    @allure.step("Создание курьера")
    def create_courier(self, login, password, first_name):
        payload = {"login": login, "password": password, "firstName": first_name}
        respons = requests.post(TotalUrl.CREATE_COURIER_URL, data=payload)
        return respons.status_code, respons.text