import configuration
import requests
import data

# Выполнить запрос на создание заказа.


def post_create_new_order(order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=order,
                         headers=data.headers)

# Получение заказа по номеру трекера.


def get_order_from_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH + str(track),
                        headers=data.headers) 

    



