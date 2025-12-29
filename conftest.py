import pytest
from generator import (
    sellerID_generator,
    name_generator,
    price_generator,
    likes_generator,
    viewCount_generator,
    contacts_generator
)
from api_requests import create_ad, del_ad_by_id

@pytest.fixture
def data_for_create_ad():
    return {
        "sellerID": sellerID_generator(),
        "name": name_generator(),
        "price": price_generator(),
        "statistics": {
            "likes": likes_generator(),
            "viewCount": viewCount_generator(),
            "contacts": contacts_generator()
        }
    }
'''
Вообще нужна данная фикстура, 
но так как очень много будет блокирующих багов из-за тела ответа созданного обьявления(структура отличается) - я позволил себе фикстуру скорректировать,
чтобы остальной функционал возможно было протестить и не перегружать базу созданными тестовыми даннами
 
@pytest.fixture
def after_create_ad_delete(data_for_create_ad):
    seller_id = data_for_create_ad.get("sellerID")
    response = create_ad(data_for_create_ad)
    response_data = response.json()
    ad_id = response_data["id"]
    yield response, seller_id, ad_id
    del_ad_by_id(ad_id)
'''

@pytest.fixture
def after_create_ad_delete(data_for_create_ad):
    seller_id = data_for_create_ad.get("sellerID")
    response = create_ad(data_for_create_ad)
    response_data = response.json()
    status_text = response_data.get("status", "")
    if " - " in status_text:
        ad_id = status_text.split(" - ")[-1]
    else:
        ad_id = None
    yield response, seller_id, ad_id, response_data
    del_ad_by_id(ad_id)


'''
#Успеть позже добавить удаление тестовых данных( в тест и фикстура
get_id = response_data["status"]
            extract_id = get_id.split(" - ")[-1]
            ad_id = response_data.get(extract_id)
            clean_up_ad.append(ad_id)
#Крадет список для сбора ID и дальнейшего удаления
@pytest.fixture
def clean_up_ad():
    ad_ids = []
    yield ad_ids
    for ad_id in ad_ids:
        if ad_id:
                del_ad_by_id(ad_id)
'''