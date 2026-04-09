# aviasales_skypro_final_task  
  
Описание проекта  
Приложение Авиасейлс создано для быстрого и удобного поиска и покупки дешёвых авиабилетов, а также для поиска отелей.  
Проект aviasales_skypro_final_task создан для автоматизации тестирования приложения Авиасейлс.  
  
Структура проекта:  
  
Aviasales_skypro_final_task  
├── config  
│   └── settings.py  
├── pages  
│   └── ClassForUI.py  
├── test  
│   ├── test_api.py  
│   └── test_ui.py  
├── .gitignore  
├── conftest.py  
├── pytest.ini  
├── README.md  
└── requirements.txt  
  
До запуска тестов рекомендуется получить и подставить cookie.  
Как получить свежие cookie:  
В браузере при поиске билета на Авиасейлс  
в DevTools  
во вкладке Network  
в таблице запросов  
появляется запрос start (только с методом не OPTION, а POST - этот запрос находится ниже),  
нужно взять из заголовков этого запроса значение x-origin-cookie  
и подставить в файл settings.py в папке config, в переменную cookie  
  
Для запуска UI-тестов ввести в терминале pytest -m ui  
Для запуска API-тестов ввести в терминале pytest -m api  
Для запуска всех тестов ввести в терминале pytest  
  
Ссылка на финальный проект:  
https://plysik973.yonote.ru/share/a3e57b68-6f6e-4d78-a25c-94c5683c1d7c  
