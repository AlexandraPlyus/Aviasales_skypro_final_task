# import time
from pages.ClassMyPage import MyPage
# time.sleep(4)


# Выпадение списка с предложенными направлениями
# def test_dropdown(driver):
#     my_page = MyPage(driver)
#     my_page.open_my_page()
#     my_page.destination_click()
#     assert my_page.is_dropdown() == True


# Появление сообщения об ошибки при пустых полях "Куда" и "Когда"
# def test_alerts(driver):
#     my_page = MyPage(driver)
#     my_page.open_my_page()
#     my_page.click_search()
#     assert my_page.is_alert_date_from() == True
#     assert my_page.is_alert_destination() == True


# Появление кадендаря при нажатиии "Когда"
# def test_calendar(driver):
#     my_page = MyPage(driver)
#     my_page.open_my_page()
#     my_page.click_start_date()
#     assert my_page.is_calendar() == True


# Появление окна информации для перелётов для введённых городов
# def test_ticket_information(driver):
#     destination = "Омск"
#     my_page = MyPage(driver)
#     my_page.open_my_page()
#     origin_city = my_page.get_origin_city()
#     my_page.input_to_destination(destination)
#     print(origin_city)
#     print(f"{origin_city}&nbsp;— {destination}")
#     print(my_page.get_ticket_information())
    # assert my_page.get_ticket_information() == f"{origin_city}&nbsp;— {destination}"


# Поиск билета
def test_get_ticket(driver):
    destination = "Омск"
    date = "2026-04-10"
    my_page = MyPage(driver)
    my_page.open_my_page()
    my_page.input_to_destination(destination)
    my_page.click_start_date()
    my_page.click_date(date)
    my_page.click_checkbox()
    my_page.click_search()
    assert my_page.result_ticket() == True



# <div class="s__On9uakoW6Azq6vqZ s__IPvmKDccjXwC4c82 s__bvxo6ZuNLncvBV0u __web-inspector-hide-shortcut__" data-test-id="text">Екатеринбург&nbsp;— Неаполь</div>
# Пустое поле назначения

# Пустые даты вылета

# Введение дат въезда и выезда.
# В полях отображаются выбранные даты соответственно

# При введении города из выпадающего списка выбрать нужный город
# и найти по нему билеты
