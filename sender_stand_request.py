import configuration
import requests
import data


def create_order(): #Создание заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.create_order_body)


def get_order_track(): #Сохранение номера созданного заказа
    order_number = str(create_order().json()['track'])
    return order_number


def get_order_by_track(): #Получаем заказ по его номеру
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_TRACK_PATH + get_order_track())






