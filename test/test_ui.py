from pages.ClassMyPage import MyPage


# Выпадение списка с предложенными направлениями
def test_dropdown(driver):
    my_page = MyPage(driver)
    my_page.open_my_page()
    my_page.destination_click()
    assert my_page.is_dropdown() is True


# Появление сообщения об ошибки при пустых полях "Куда" и "Когда"
def test_alerts(driver):
    my_page = MyPage(driver)
    my_page.open_my_page()
    my_page.click_search()
    assert my_page.is_alert_destination() is True
    assert my_page.is_alert_date_form() is True


# Появление кадендаря при нажатиии "Когда"
def test_calendar(driver):
    my_page = MyPage(driver)
    my_page.open_my_page()
    my_page.click_start_date()
    assert my_page.is_calendar() is True


# Появление окна информации для перелётов для введённых городов
def test_ticket_information(driver):
    destination = "Томск"
    my_page = MyPage(driver)
    my_page.open_my_page()
    origin_city = my_page.get_origin_city()
    my_page.input_to_destination(destination)
    ticket_info = my_page.get_ticket_information(origin_city, destination)
    assert origin_city in ticket_info and destination in ticket_info


# Поиск билета
def test_get_ticket(driver):
    origin_city = "Москва"
    destination = "Омск"
    date = "08.04.2026"
    my_page = MyPage(driver)
    my_page.open_my_page()
    my_page.input_to_origin_city(origin_city)
    my_page.input_to_destination(destination)
    my_page.click_start_date()
    my_page.click_date(date)
    my_page.click_checkbox()
    my_page.click_search()
    assert my_page.result_search() is True
