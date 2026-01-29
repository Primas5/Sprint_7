from methods.courier_methods import CourierMeth
import allure
from helpers import generate_data_for_courier
from data import Data

class TestCourierRegister:

    @allure.title("Создание курьера")
    def test_create_courier_is_created(self, create_courier_and_delete):
        courier_data = create_courier_and_delete
        st_code, create_result = CourierMeth().create_courier(
            courier_data[0],
            courier_data[1],
            courier_data[2]
        )
        assert (st_code == 201)
        assert (create_result == Data.COURIER_CREATION_ANSWER)

    @allure.title("Создание курьера с тем же логином")
    def test_creating_courier_with_the_same_login_is_denied(self, create_courier_and_delete):
        courier_data = create_courier_and_delete
        created_courier = CourierMeth().create_courier(
            courier_data[0],
            courier_data[1],
            courier_data[2]
        )
        created_courier = CourierMeth().create_courier(
            courier_data[0],
            courier_data[1],
            courier_data[2]
        )
        assert (created_courier[0] == 409)
        assert (created_courier[1] == Data.COURIER_ALREADY_EXIST_ANSWER)

    @allure.title("Создание курьера без логина")
    def test_creating_courier_without_login_is_denied(self):

        data_courier = generate_data_for_courier()
        created_courier = CourierMeth().create_courier(
            "", 
            data_courier[1], 
            data_courier[2]
        )
        assert (created_courier[0] == 400)
        assert (created_courier[1] == Data.COURIER_CREATION_MISSED_DATA_ANSWER)

    @allure.title("Создание курьера без пароля")
    def test_creating_courier_without_password_is_denied(self):

        data_courier = generate_data_for_courier()
        created_courier = CourierMeth().create_courier(
            data_courier[0], 
            "",
            data_courier[2]
        )
        assert (created_courier[0] == 400)
        assert (created_courier[1] == Data.COURIER_CREATION_MISSED_DATA_ANSWER)

    @allure.title("Создание курьера без имени")
    def test_creating_courier_without_first_name_is_denied(self,create_courier_and_delete):
        data_courier = create_courier_and_delete
        created_courier = CourierMeth().create_courier(
            data_courier[0],
            data_courier[1],
            ""
        )
        assert (created_courier[0] == 201)
        assert (created_courier[1] == Data.COURIER_CREATION_ANSWER)