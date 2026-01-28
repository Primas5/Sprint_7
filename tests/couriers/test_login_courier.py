from methods.courier_methods import CourierMeth
from data import Data
import allure


class TestCourierLogin:

    @allure.title("Логин курьера с валидными данными")
    def test_login_courier_is_successful(self, create_courier_and_delete):
        st_code, create_result, courier_data = create_courier_and_delete
        login_courier = CourierMeth().login_courier(
            courier_data[0],
            courier_data[1]
        )
        assert login_courier[0] == 200
        assert login_courier[1]["id"] is not None

    @allure.title("Логин курьера с отсутствующим логином")
    def test_login_courier_withot_login_is_denied(self):
        login_courier = CourierMeth().login_courier(
            "", 
            Data.COURIER_CREDENTIALS["password"]
        )
        assert (login_courier[0] == 400)
        assert (login_courier[1]["message"] == Data.COURIER_NOT_ENOUGH_DATA_FOR_LOGIN)

    @allure.title("Логин курьера с отсутствующим паролем")
    def test_login_courier_withot_password_is_denied(self):
        login_courier = CourierMeth().login_courier(
            Data.COURIER_CREDENTIALS["login"], 
            ""
        )
        assert (login_courier[0] == 400)
        assert (login_courier[1]["message"] == Data.COURIER_NOT_ENOUGH_DATA_FOR_LOGIN)

    @allure.title("Логин курьера с отсутствующим логином и паролем")
    def test_login_courier_withot_login_and_password_is_denied(self):
        login_courier = CourierMeth().login_courier(
            "", 
            ""
        )
        assert (login_courier[0] == 400)
        assert (login_courier[1]["message"] == Data.COURIER_NOT_ENOUGH_DATA_FOR_LOGIN)

    @allure.title("Логин курьера с неверным логином")
    def test_login_courier_with_incorrect_login_is_denied(self):
        login_courier = CourierMeth().login_courier(
            Data.COURIER_WRONG_DATA,
            Data.COURIER_CREDENTIALS["password"]
        )
        assert (login_courier[0] == 404)
        assert (login_courier[1]["message"] == Data.COURIER_PROFILE_NOT_FOUND)

    @allure.title("Логин курьера с неверным паролем")
    def test_login_courier_with_incorrect_password_is_denied(self):
        login_courier = CourierMeth().login_courier(
            Data.COURIER_CREDENTIALS["login"], 
            Data.COURIER_WRONG_DATA
        )
        assert (login_courier[0] == 404)
        assert (login_courier[1]["message"] == Data.COURIER_PROFILE_NOT_FOUND)