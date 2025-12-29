import pytest
import allure
from api_requests import create_ad
from data import InvalidField, MissingField, MissingFieldStatistics, ZeroInField

class TestCreateAd:
    @allure.title("TC001-Тест создание обьявления")
    def test_create_ad(self, data_for_create_ad):
        response = create_ad(data_for_create_ad)
        assert response.status_code == 200
        response_data = response.json()
        assert "id" in response_data , f" получен {response.json()}"
        assert "sellerId" in response_data
        assert "name" in response_data
        assert "price" in response_data
        assert "statistics" in response_data
        assert "createdAt" in response_data
        stats = response_data["statistics"]
        assert "likes" in stats
        assert "viewCount" in stats
        assert "contacts" in stats

    @allure.title("TC002-Тест создание обьявления с тем же идентификатором продавца")
    def test_create_ad_double_seller_id(self, data_for_create_ad):
        seller_id = data_for_create_ad["sellerID"]
        response = create_ad(data_for_create_ad)
        with allure.step(f"Проверить успешное создание первого обьявления"):
            assert response.status_code == 200
            response_data1 = response.json()

            data_ad = data_for_create_ad.copy()
            data_ad["sellerID"] = seller_id
            response = create_ad(data_ad)
        with allure.step(f"Проверить успешное создание второго обьявления с тем же sellerid первого обьявления"):
            assert response.status_code == 200
            response_data2 = response.json()

            assert response_data1 != response_data2
            assert "id" in response_data2, f" получен {response.json()}"
            assert "sellerId" in response_data2
            assert "name" in response_data2
            assert "price" in response_data2
            assert "statistics" in response_data2
            assert "createdAt" in response_data2
            stats = response_data2["statistics"]
            assert "likes" in stats
            assert "viewCount" in stats
            assert "contacts" in stats

    @pytest.mark.parametrize("field_name, test_case_id", ZeroInField.field)
    @allure.title("{test_case_id}-Тест создание объявления с нулевым значением {field_name}")
    def test_create_ad_with_zero_value_fields(self, data_for_create_ad, field_name, test_case_id):
        data_ad = data_for_create_ad.copy()
        if field_name == "price":
            data_ad["price"] = 0
        else:
            data_ad["statistics"][field_name] = 0
        response = create_ad(data_ad)
        with allure.step(f"{test_case_id}-Проверить успешное создание с {field_name}=0"):
            assert response.status_code == 200
            response_data = response.json()

            assert "id" in response_data, f" получен {response.json()}"
            assert "sellerId" in response_data
            assert "name" in response_data
            assert "price" in response_data
            assert "statistics" in response_data
            assert "createdAt" in response_data
            stats = response_data["statistics"]
            assert "likes" in stats
            assert "viewCount" in stats
            assert "contacts" in stats

    @pytest.mark.parametrize("field, id_test_case", MissingField.field)
    @allure.title("{id_test_case}-Тест создания обьявления с отсутствующим обязательным полем")
    def test_registration_with_missing_field(self, data_for_create_ad, field, id_test_case):
        data_ad = data_for_create_ad.copy()
        del data_ad[field]
        response = create_ad(data_ad)
        with allure.step(f"{id_test_case}-Проверить возможность создания с {field}"):
            assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"
        with allure.step("Проверить сообщение об ошибке"):
            response_data = response.json()
            assert "result" in response_data
            assert "status" in response_data


    @pytest.mark.parametrize("field, id_test_case", MissingFieldStatistics.field)
    @allure.title("{id_test_case}-Тест создания обьявления с отсутствующим обязательным полем в statistics")
    def test_registration_with_missing_statistics_field(self, data_for_create_ad, field, id_test_case):
        data_ad = data_for_create_ad.copy()
        del data_ad["statistics"][field]
        response = create_ad(data_ad)
        with allure.step(f"{id_test_case}-Проверить возможность создания с {field}"):
            assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"
        with allure.step("Проверить сообщение об ошибке"):
            response_data = response.json()
            assert "result" in response_data
            assert "status" in response_data

    @pytest.mark.parametrize("field, invalid_value, id_test_case", InvalidField.invalid_fields)
    @allure.title("{id_test_case}-Тест создание объявления с невалидным значением параметра {field} равный {invalid_value}")
    def test_create_ad_with_invalid_fields(self, data_for_create_ad, field, invalid_value, id_test_case):
        data_ad = data_for_create_ad.copy()
        data_ad[field] = invalid_value
        response = create_ad(data_ad)
        with allure.step(f"{id_test_case}-Проверить статус код 400"):
            assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"
        with allure.step("Проверить сообщение об ошибке"):
            response_data = response.json()
            assert "result" in response_data
            assert "status" in response_data

    @pytest.mark.parametrize("static_field, invalid_value, id_test_case", InvalidField.statistics_fields)
    @allure.title("{id_test_case}-Тест создание с невалидным statistics.{stat_field} равный {invalid_value}")
    def test_create_ad_with_invalid_static_field(self, data_for_create_ad, static_field, invalid_value, id_test_case):
        data_ad = data_for_create_ad.copy()
        data_ad["statistics"][static_field] = invalid_value
        response = create_ad(data_ad)
        with allure.step(f"{id_test_case}-Проверить статус код 400"):
            assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"
        with allure.step("Проверить сообщение об ошибке"):
            response_data = response.json()
            assert "result" in response_data
            assert "status" in response_data

    @allure.title("ТС054-Тест создание объявления с дополнительным параметром address")
    def test_create_ad_with_extra_field(self, data_for_create_ad):
        data_ad = data_for_create_ad.copy()
        data_ad["address"] = "Крылова"
        response = create_ad(data_ad)
        with allure.step("Проверить статус код 400"):
            assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"
        with allure.step("Проверить сообщение об ошибке"):
            response_data = response.json()
            assert "result" in response_data
            assert "status" in response_data