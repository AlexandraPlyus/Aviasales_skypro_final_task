# import time
from pages.ClassMyPage import MyPage
# time.sleep(4)


def testinput_to_destin(driver):
    destination = "Омск"
    my_page = MyPage(driver)
    my_page.open_my_page()

    assert my_page.input_to_destination(destination) == destination


# def empty_destination(driver):
#     # date_start = 
#     my_page = MyPage(driver)
#     my_page.click_checkbox()
#     my_page.input_to_destination("")
#     # my_page.input_to_start_date()
#     my_page.click_search()

#     assert 


















# Пустое поле назначения

# Пустые даты вылета

# Введение дат въезда и выезда.
# В полях отображаются выбранные даты соответственно


# При введении города из выпадающего списка выбрать нужный город
# и найти по нему билеты
