import pytest
from methods.order_methods import OrderMeth
import allure
from helpers import generate_data_for_order

from data import Data


class TestOrder:

    @allure.title("Создание заказа с разными цветами")
    @pytest.mark.parametrize(
        "color",
        [Data.ORDER_DATA_NO_COLOR, Data.ORDER_DATA_BLACK, Data.ORDER_DATA_GREY, Data.ORDER_DATA_BOTH]
    )
    def test_creatin_order_now_color_successful(self, color):

        data_order = generate_data_for_order()
        response = OrderMeth().create_order(data_order, color)
        assert response[0] == 201
        assert response[1]["track"] is not None
