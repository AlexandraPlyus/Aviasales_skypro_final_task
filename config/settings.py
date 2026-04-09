class APIConfig:
    """Конфигурация для API тестов"""

    cookie = ''
    tickets = "https://tickets-api.aviasales.ru/search/v2/start"
    referer = "https://www.aviasales.ru/"

    origin_city = "BQS"
    destination = "UUS"

    # Дата на год вперёд от сегодня
    date_year_ahead = "2027-04-08"
    # Дата на 5-7 дней вперёд от сегодня
    date = "2026-04-13"
    # Дата возвращения на день раньше Даты
    return_date = "2026-04-12"
    # Несуществующая дата
    non_existent_date = "2026-13-07"


class UIConfig:
    """Конфигурация для UI тестов"""
    BASE_URL = "https://www.aviasales.ru/"
    date = "15.04.2026"
    origin_city = "Москва"
    destination = "Омск"
