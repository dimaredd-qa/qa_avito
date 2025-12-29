import pytest
import allure
from api_requests import create_ad, get_ad_by_id
from data import InvalidField

class TestGetAdById:
    @allure.title("ТС055-Тест получение обьявления по его идентификатору")
    def test_get_ad_by_id_after_create(self, after_create_ad_delete):
        response = get_ad_by_id(after_create_ad_delete[2])
        with allure.step(f"Проверить получения обьявления по его id"):
            assert response.status_code == 200
            response_data = response.json()
            ad = response_data[0]
            assert "id" in ad, f" получен {response.json()}"
            assert "sellerId" in ad
            assert "name" in ad
            assert "price" in ad
            assert "statistics" in ad
            stats = ad["statistics"]
            assert "likes" in stats
            assert "viewCount" in stats
            assert "contacts" in stats
            assert "createdAt" in ad

    @pytest.mark.parametrize("invalid_id, id_test_case", InvalidField.invalid_get_ad_by_id)
    @allure.title("{id_test_case}-Тест запроса несуществующего/невалидного id: {invalid_id}")
    def test_create_ad_with_invalid_static_field(self, after_create_ad_delete, invalid_id, id_test_case):
        response = get_ad_by_id(invalid_id)
        with allure.step(f"Проверить возможность получения обьявления при невалидном id: {invalid_id}"):
            assert response.status_code == 400 or response.status_code == 404
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
                assert "status" in response_data