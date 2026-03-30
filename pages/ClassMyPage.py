from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC


class MyPage:
    BASE_URL = "https://www.aviasales.ru/"

    INPUT_DESTIN = (By.ID, "avia_form_destination-input")

    DROPDOWN = (By.XPATH, "// ul[ @ id = 'avia_form_destination-menu']")

    CHECKBOX = (
        By.CSS_SELECTOR, 'label[data-test-id="checkbox"] >' +
        'input[type=checkbox]'
    )

    SEARCH = (By.CSS_SELECTOR, '[type="button"][data-test-id="form-submit"]')

    DESTIN_ALERT = (
        By.XPATH, "//div[@data-test-id='text' and" +
        "text()='Укажите город прибытия']"
        )

    DATE_FROM_ALERT = (
        By.XPATH, "//div[@data-test-id='text' and text()='Укажите дату']"
    )

    ORIRGIN_INPUT = (By.XPATH, "//input[@id='avia_form_origin-input']")

    START_DATE = (By.XPATH, '//button[@data-test-id="start-date-field"]')

    CALENDAR = (By.XPATH, '//div[@data-multiple-months="true"]')

    TICKET_INFORMATION = (
        By.CSS_SELECTOR, 'aside > div > nav > div[data-test-id="text"]'
    )

    DATE = (By.XPATH, '//td[@data-day={date}]')

    SAVE_SEARCH = (
        By.CSS_SELECTOR, '[data-test-id="text"][text()="Сохранить поиск"]'
    )

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_my_page(self):
        # Открывает страницу
        self.driver.execute_cdp_cmd(
            'Page.setLifecycleEventsEnabled', {'enabled': False}
        )
        self.driver.get(self.BASE_URL)

        self.wait.until(
            EC.presence_of_element_located(self.INPUT_DESTIN)
        )

    def destination_click(self):
        # Нажимает на поле города назначения
        self.wait.until(
            EC.presence_of_element_located(self.INPUT_DESTIN)
        ).click()

    def input_to_destination(self, sity):
        # Вводит название города назначения
        destination = self.wait.until(
            EC.presence_of_element_located(self.INPUT_DESTIN)
        )
        # Очищаем поле ввода
        destination.clear()
        # Вводим название
        destination.send_keys(sity)
        self.wait.until(
            EC.presence_of_element_located(self.DROPDOWN)).click()

    def is_dropdown(self):
        # Проверяет наличие dropdown на странице
        try:
            self.wait.until(EC.presence_of_element_located(self.DROPDOWN))
            return True
        except Exception as e:
            print(f"Dropdown не найден: {e}")
            return False

    def is_alert_date_from(self):
        # Проверяет наличие ошибки: отсутствие даты вылета
        try:
            self.wait.until(
                EC.presence_of_element_located(self.DATE_FROM_ALERT)
            )
            return True
        except Exception as e:
            print(f"Alert не найден: {e}")
            return False

    def is_alert_destination(self):
        # Проверяет наличие ошибки: отсутствие города назначения
        try:
            self.wait.until(EC.presence_of_element_located(self.DESTIN_ALERT))
            return True
        except Exception as e:
            print(f"Alert город назначения не найден: {e}")
            return False

    def click_checkbox(self):
        # Нажимает на чекбокс Островка
        self.wait.until(EC.presence_of_element_located(self.CHECKBOX)).click()

    def click_search(self):
        # Нажимает поиск
        self.wait.until(EC.presence_of_element_located(self.SEARCH)).click()

    def click_start_date(self):
        # Нажимает на дату вылета
        self.wait.until(
            EC.presence_of_element_located(self.START_DATE)
        ).click()

    def is_calendar(self):
        # Проверяет наличие calendar на странице
        try:
            self.wait.until(EC.presence_of_element_located(self.CALENDAR))
            return True
        except Exception as e:
            print(f"Календарь не найден: {e}")
            return False

    def get_origin_city(self):
        # Возвращает значение из поля 'Откуда'
        origin_input = self.wait.until(
            EC.presence_of_element_located(self.ORIRGIN_INPUT)
        )
        value = origin_input.get_attribute('value')
        print(f"Город отправления: {value}")
        return value

    def get_ticket_information(self):
        # Ждать появления этого окошка
        divs = self.wait.until(
            EC.presence_of_element_located(self.TICKET_INFORMATION)
        )
        # divs = self.driver.find_elements(self.TICKET_INFORMATION)
        divs_list = [div.text() for div in divs]
        return divs_list[2]

    def click_date(self, date):
        # Нажимает на кнопку с введённой датой
        self.wait.until(EC.presence_of_element_located(self.DATE)).click()

    def result_ticket(self):
        # Проверяет наличие элемента "Сохранить поиск"
        try:
            self.wait.until(EC.presence_of_element_located(self.SAVE_SEARCH))
            return True
        except Exception as e:
            print(f"Сохранить поиск - не найдено, {e}")
            return False
