import configuration
import requests


# Создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)


# Получение заказа по его треку
def get_new_user_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK, params={"t": track})
