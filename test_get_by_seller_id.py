import pytest
import allure
from api_requests import get_ads_by_seller_id
from data import InvalidField


class TestGetAdBySellerId:
    @allure.title("ТС060-Тест получения имеющихся объявлений у продавца")
    def test_get_exist_ad_by_seller_id(self, after_create_ad_delete):
        response = get_ads_by_seller_id(after_create_ad_delete[1])
        assert response.status_code == 200
        response_data = response.json()
        ad = response_data[0]
        assert "id" in ad, f" получен {response.json()}"
        assert "sellerId" in ad
        assert "name" in ad
        assert "price" in ad
        assert "statistics" in ad
        stats =ad["statistics"]
        assert "likes" in stats
        assert "viewCount" in stats
        assert "contacts" in stats
        assert "createdAt" in ad

    @allure.title("ТС061-Тест получения обьявлений по идентификатору продавца без обьявлений ")
    def test_get_missing_ad_by_seller_id(self, data_for_create_ad):
        empty_seller_id = data_for_create_ad["sellerID"]
        response = get_ads_by_seller_id(empty_seller_id)
        assert response.status_code == 200
        assert response.json() == []

    @allure.title("{test_case}-Тест запроса с невалидным значением sellerID")
    @pytest.mark.parametrize("invalid_seller_id, test_case", InvalidField.invalid_seller_id_for_get)
    def test_get_ad_with_invalid_seller_id(self, invalid_seller_id, test_case):
        response = get_ads_by_seller_id(invalid_seller_id)
        with allure.step(f"{test_case}-Проверить код ответа 400 Bad Request"):
            assert response.status_code == 400 or response.status_code == 404, f"Ожидался 400 или 404, получен {response.status_code}"
            if response.status_code == 400:
                response_data = response.json()
                assert "result" in response_data
                res = response_data["result"]
                assert "messages" in res
                assert "message" in res
                assert "status" in response_data
            elif response.status_code == 404:
                response_data = response.json()
                assert "result" in response_data
                res = response_data["result"]
                assert "messages" in res
                assert "message" in res
                assert "status" in response_data