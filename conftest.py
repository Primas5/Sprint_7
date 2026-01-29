import pytest
from helpers import generate_data_for_courier
from methods.courier_methods import CourierMeth

@pytest.fixture
def create_courier_and_delete():
    """Фикстура для удаления курьера"""
    data = generate_data_for_courier()
    yield data
    currentcode, currentdata = CourierMeth().login_courier(data[0], data[1])
    currentid = currentdata["id"]
    CourierMeth().delete_courier(currentid)
