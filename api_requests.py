import allure
import requests

from data import Endpoint

@allure.step("Создание обьявления")
def create_ad(data_ad):
    response = requests.post(Endpoint.create_ad_url, json=data_ad)
    return response

@allure.step("Получить объявление по id")
def get_ad_by_id(ad_id):
    url = Endpoint.get_ad_by_id.format(ad_id=ad_id)
    response = requests.get(url)
    return response

@allure.step("Удалить объявление по id")
def del_ad_by_id(del_id):
    url = Endpoint.del_ad_by_id.format(del_id=del_id)
    response = requests.delete(url)
    return response

@allure.step("Получить объявления по sellerID продавца")
def get_ads_by_seller_id(seller_id):
    url = Endpoint.get_ads_by_seller_id.format(seller_id=seller_id)
    response = requests.get(url)
    return response

@allure.step("Получить статистику по id v1")
def get_statistic_v1(stat_id):
    url = Endpoint.get_statistic_v1.format(stat_id=stat_id)
    response = requests.get(url)
    return response

@allure.step("Получить статистику по id v2")
def get_statistic_v2(stat_id):
    url = Endpoint.get_statistic_v2.format(stat_id=stat_id)
    response = requests.get(url)
    return response