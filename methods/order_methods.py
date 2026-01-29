import requests
from urls import TotalUrl
import allure

class OrderMeth:

    @allure.step("Создание заказа")
    def create_order(self, order_data, color):
        payload = {
            "firstName": order_data[0],
            "lastName": order_data[1],
            "address": order_data[2],
            "metroStation": order_data[3],
            "phone": order_data[4],
            "rentTime": order_data[5],
            "deliveryDate": order_data[6],
            "comment": order_data[7],
            "color": color,
        }
        respons = requests.post(TotalUrl.CREATING_ORDER_URL, json=payload)
        return respons.status_code, respons.json()

    @allure.step("Порлучение заказа")
    def get_order(self, curied_id=None, nearestStation=None, limit=None, page=None):
        payload = {
            "courierId": curied_id,
            "nearestStation": nearestStation,
            "limit": limit,
            "page": page,
        }
        respons = requests.get(TotalUrl.ORDERS_URL, data=payload)
        return respons.status_code, respons.json()
