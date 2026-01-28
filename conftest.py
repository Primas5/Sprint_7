import pytest
from helpers import generate_data_for_courier
from methods.courier_methods import CourierMeth

@pytest.fixture
def create_courier_and_delete():
    """Фикстура для создания и удаления курьера"""
    data = generate_data_for_courier()

    st_code,create_result = CourierMeth().create_courier(data[0],data[1],data[2])
    if st_code != 201:
        pytest.skip(f"Не удалось создать курьера: {st_code}")
    yield st_code, create_result, data
    currentcode, currentdata = CourierMeth().login_courier(data[0], data[1])
    currentid = currentdata["id"]
    CourierMeth().delete_courier(currentid)
