
class Data:
    COURIER_CREDENTIALS = {
        "login": "adoroshin",
        "password": "doroshin123",
        "firstName": "Aleksey",
    }
    COURIER_WRONG_DATA = "wrongpassorlogin"

    ORDER_DATA_NO_COLOR = []
    ORDER_DATA_BLACK = ["BLACK"]
    ORDER_DATA_GREY = ["GREY"]
    ORDER_DATA_BOTH = ["BLACK", "GREY"]

    COURIER_NOT_ENOUGH_DATA_FOR_LOGIN = "Недостаточно данных для входа"
    COURIER_PROFILE_NOT_FOUND = "Учетная запись не найдена"
    COURIER_CREATION_ANSWER = '{"ok":true}'
    COURIER_ALREADY_EXIST_ANSWER = ('{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}')
    COURIER_CREATION_MISSED_DATA_ANSWER = ('{"code":400,"message":"Недостаточно данных для создания учетной записи"}')