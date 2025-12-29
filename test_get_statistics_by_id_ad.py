import pytest
import allure
from api_requests import get_statistic_v1, get_statistic_v2

class TestGetStatistic:

    @allure.title("ТС064 - Успешный запрос на получение статистики у существующего объявления v1")
    def test_get_statistic_v1_success(self, after_create_ad_delete):
        response = get_statistic_v1(after_create_ad_delete[2])
        assert response.status_code == 200
        response_data = response.json()
        stat_ad = response_data[0]
        assert "likes" in stat_ad
        assert "viewCount" in stat_ad
        assert "contacts" in stat_ad

    @allure.title("ТС065 - Успешный запрос на получение статистики у существующего объявления v2")
    def test_get_statistic_v2_success(self, after_create_ad_delete):
        response = get_statistic_v2(after_create_ad_delete[2])
        assert response.status_code == 200
        response_data = response.json()
        stat_ad = response_data[0]
        assert "likes" in stat_ad
        assert "viewCount" in stat_ad
        assert "contacts" in stat_ad

    @allure.title("ТС066 - Запрос с несуществующей ID объявления v2")
    def test_get_statistic_v1_not_found(self):
        non_existent_id = "97928230-9999-9999-9999717"
        response = get_statistic_v1(non_existent_id)
        assert response.status_code in [400, 404], f"Ожидался 400 или 404, получен {response.status_code}"
        if response.status_code in [400, 404]:
            response_data = response.json()
            assert "result" in response_data
            assert "status" in response_data

    @allure.title("ТС067 - Запрос с несуществующей ID объявления v2")
    def test_get_statistic_v2_not_found(self):
        non_existent_id = "97928230-9999-9999-9999717"
        response = get_statistic_v2(non_existent_id)
        assert response.status_code in [400, 404], f"Ожидался 400 или 404, получен {response.status_code}"
        if response.status_code in [400, 404]:
            response_data = response.json()
            assert "result" in response_data
            assert "status" in response_data