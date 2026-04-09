import allure
import pytest
from pages.ClassForUI import MyPage
from selenium.webdriver.remote.webdriver import WebDriver
from config.settings import UIConfig

ui_class = UIConfig
date = ui_class.date
origin_city = ui_class.origin_city
destination = ui_class.destination


@pytest.mark.ui
@allure.title("Выпадение списка с предложенными направлениями")
@allure.story("Поиск билетов")
@allure.feature("Позитивные проверки")
def test_dropdown(driver: WebDriver):
    my_page = MyPage(driver)
    with allure.step("Открыть главную страницу"):
        my_page.open_my_page()
    with allure.step("Кликнуть по полю 'Куда'"):
        my_page.destination_click()
    with allure.step(
        "Проверить, что выпадающий список с" +
        "предложенными направлениями отобразился"
    ):
        assert my_page.is_dropdown() is True


@pytest.mark.ui
@allure.title(
    "Появление сообщения об ошибки при пустых полях 'Куда' и 'Когда'"
)
@allure.story("Поиск билетов")
@allure.feature("Позитивные проверки")
def test_alerts(driver: WebDriver):
    my_page = MyPage(driver)
    with allure.step("Открыть главную страницу"):
        my_page.open_my_page()
    with allure.step("Нажать кнопку 'Найти билеты'"):
        my_page.click_search()
    with allure.step(
        "Проверить, что появилось сообщение об ошибке для поля 'Куда'"
    ):
        assert my_page.is_alert_destination() is True
    with allure.step(
        "Проверить, что появилось сообщение об ошибке для поля 'Когда'"
    ):
        assert my_page.is_alert_date_form() is True


@pytest.mark.ui
@allure.title("Появление кадендаря при нажатиии 'Когда'")
@allure.story("Поиск билетов")
@allure.feature("Позитивные проверки")
def test_calendar(driver: WebDriver):
    my_page = MyPage(driver)
    with allure.step("Открыть главную страницу"):
        my_page.open_my_page()
    with allure.step("Кликнуть по полю 'Когда'"):
        my_page.click_start_date()
    with allure.step("Проверить, что календарь отобразился"):
        assert my_page.is_calendar() is True


@pytest.mark.ui
@allure.title("Появление окна информации для перелётов для введённых городов")
@allure.story("Поиск билетов")
@allure.feature("Позитивные проверки")
def test_ticket_information(driver: WebDriver):
    my_page = MyPage(driver)
    with allure.step("Открыть главную страницу"):
        my_page.open_my_page()
    with allure.step(f"Ввести город отправления: {origin_city}"):
        my_page.input_to_origin_city(origin_city)
    with allure.step(f"Ввести город назначения: {destination}"):
        my_page.input_to_destination(destination)
    with allure.step("Получить информацию о перелёте"):
        ticket_info = my_page.get_ticket_information(origin_city, destination)
    with allure.step(
        "Проверить, что окно информации содержит введённые города"
    ):
        assert origin_city in ticket_info and destination in ticket_info


@pytest.mark.ui
@allure.title("Поиск билета")
@allure.story("Поиск билетов")
@allure.feature("Позитивные проверки")
def test_get_ticket(driver: WebDriver):
    my_page = MyPage(driver)
    with allure.step("Открыть главную страницу"):
        my_page.open_my_page()
    with allure.step(f"Ввести город отправления: {origin_city}"):
        my_page.input_to_origin_city(origin_city)
    with allure.step(f"Ввести город назначения: {destination}"):
        my_page.input_to_destination(destination)
    with allure.step("Открыть календарь выбора даты"):
        my_page.click_start_date()
    with allure.step(f"Выбрать дату: {date}"):
        my_page.click_date(date)
    with allure.step("Поставить галоку (чекбокс)"):
        my_page.click_checkbox()
    with allure.step("Нажать кнопку 'Найти билеты'"):
        my_page.click_search()
    with allure.step("Проверить, что результаты поиска отобразились"):
        assert my_page.result_search() is True
