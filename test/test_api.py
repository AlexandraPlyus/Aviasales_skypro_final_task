import allure
import pytest
import requests
from config.settings import APIConfig

api_class = APIConfig

cookie = api_class.cookie
tickets = api_class.tickets
referer = api_class.referer
origin_city = api_class.origin_city
destination = api_class.destination

# Дата на год вперёд от сегодня
date_year_ahead = api_class.date_year_ahead
# Дата на 5-7 дней вперёд от сегодня
date = api_class.date
# Дата возвращения на день раньше Даты
return_date = api_class.return_date
# Несуществующая дата
non_existent_date = api_class.non_existent_date


@pytest.mark.api
@allure.title("Поиск билета на год вперёд")
@allure.story("Поиск билетов")
@allure.feature("Позитивные проверки")
def test_search_ticket_year_ahead():
    headers = {"Referer": referer, "Cookie": cookie}
    body = {
        "currency_code": "rub",
        "marker": "direct",
        "search_params": {
            "directions": [
                {
                    "origin": origin_city,
                    "destination": destination,
                    "date": date_year_ahead,
                }
            ],
            "passengers": {"adults": 1},
            "trip_class": "Y",
        },
    }
    with allure.step("Отправить POST запрос к API для поиска билетов"):
        response = requests.post(tickets, json=body, headers=headers)
    with allure.step("Распарсить JSON ответ"):
        body_response = response.json()

    with allure.step("Проверить, что статус-код ответа равен 200"):
        assert response.status_code == 200
    with allure.step(
        "Проверить, что в ответе присутствует непустой search_id"
    ):
        assert "search_id" in body_response and body_response["search_id"]


@pytest.mark.api
@allure.title("Поиск авиабилета на 0 человек")
@allure.story("Поиск билетов")
@allure.feature("Негативные проверки")
def test_search_for_zero_adults():
    headers = {"Referer": referer, "Cookie": cookie}
    body = {
        "currency_code": "rub",
        "marker": "direct",
        "search_params": {
            "directions": [
                {
                    "origin": origin_city,
                    "destination": destination,
                    "date": date,
                }
            ],
            "passengers": {"adults": 0},
            "trip_class": "Y",
        },
    }
    with allure.step("Отправить POST запрос к API для поиска билетов"):
        response = requests.post(tickets, json=body, headers=headers)
    with allure.step("Распарсить JSON ответ"):
        body_response = response.json()

    with allure.step("Проверить, что статус-код ответа равен 400"):
        assert response.status_code == 400
    with allure.step(
        "Проверить, что в ответе присутствует сообщение" +
        "об ошибке '0' пассажиров"
    ):
        assert (
            body_response["message"]
            == 'unexpected number of adult passengers "0"'
        )


@pytest.mark.api
@allure.title("Поиск перелёта на 10 человек")
@allure.story("Поиск билетов")
@allure.feature("Негативные проверки")
def test_search_for_ten_adults():
    headers = {"Referer": referer, "Cookie": cookie}

    body = {
        "currency_code": "rub",
        "marker": "direct",
        "search_params": {
            "directions": [
                {
                    "origin": origin_city,
                    "destination": destination,
                    "date": date,
                }
            ],
            "passengers": {"adults": 10},
            "trip_class": "Y",
        },
    }
    with allure.step("Отправить POST запрос к API для поиска билетов"):
        response = requests.post(tickets, json=body, headers=headers)
    with allure.step("Распарсить JSON ответ"):
        body_response = response.json()
    with allure.step("Проверить, что статус-код ответа равен 400"):
        assert response.status_code == 400
    with allure.step(
        "Проверить, что в ответе присутствует сообщение" +
        "об ошибке '10' пассажиров"
    ):
        assert (
            body_response["message"]
            == 'unexpected number of adult passengers "10"'
        )


@pytest.mark.api
@allure.title("Поиск перелётов с датой возвращения раньше даты вылета")
@allure.story("Поиск билетов")
@allure.feature("Негативные проверки")
def test_search_return_date_earlier():
    headers = {"Referer": referer, "Cookie": cookie}

    body = {
        "currency_code": "rub",
        "marker": "direct",
        "search_params": {
            "directions": [
                {
                    "origin": origin_city,
                    "destination": destination,
                    "date": date,
                },
                {
                    "origin": destination,
                    "destination": origin_city,
                    "date": return_date,
                },
            ],
            "passengers": {"adults": 1},
            "trip_class": "Y",
        },
    }
    with allure.step("Отправить POST запрос к API для поиска билетов"):
        response = requests.post(tickets, json=body, headers=headers)
    with allure.step("Распарсить JSON ответ"):
        body_response = response.json()
    with allure.step("Проверить, что статус-код ответа равен 400"):
        assert response.status_code == 400
    with allure.step(
        "Проверить, что в ответе присутствует" +
        "сообщение об ошибке неожиданный порядок указаний"
    ):
        assert body_response["message"] == "unexpected order of directions"


@pytest.mark.api
@allure.title("Поиск билета на несуществующую дату")
@allure.story("Поиск билетов")
@allure.feature("Негативные проверки")
def test_search_non_existent_date():
    headers = {"Referer": referer, "Cookie": cookie}

    body = {
        "currency_code": "rub",
        "marker": "direct",
        "search_params": {
            "directions": [
                {
                    "origin": origin_city,
                    "destination": destination,
                    "date": non_existent_date,
                }
            ],
            "passengers": {"adults": 1},
            "trip_class": "Y",
        },
    }
    with allure.step("Отправить POST запрос к API для поиска билетов"):
        response = requests.post(tickets, json=body, headers=headers)
    with allure.step("Распарсить JSON ответ"):
        body_response = response.json()
    with allure.step("Проверить, что статус-код ответа равен 400"):
        assert response.status_code == 400
    with allure.step(
        "Проверить, что в ответе присутствует" +
        "сообщение об ошибке 'invalid-arguments'"
    ):
        assert "invalid-arguments" in str(body_response)
    with allure.step(
        "Проверить, что в ответе присутствует" +
        "несуществующая дата: {non_existent_date}"
    ):
        assert f"{non_existent_date}" in str(body_response).lower()
