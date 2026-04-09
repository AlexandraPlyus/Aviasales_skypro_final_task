# aviasales_skypro_final_task

Как использовать зависимости из файла requirements.txt:
Ввести в терминале VScode поочерёдно команды:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Как получить свежие cookie:
В браузере при поиске билета на Авиасейлс 
в DevTools 
во вкладке Network 
в таблице запросов 
появляется запрос start (только не OPTION, а с методом POST - этот запрос находится ниже), 
нужно взять из заголовков этого запроса значение x-origin-cookie 
и подставить в файл test_api.py в переменную cookie

Для запуска UI-тестов ввести в терминале pytest -m ui
Для запуска API-тестов ввести в терминале pytest -m api
Для запуска всех тестов ввести в терминале pytest