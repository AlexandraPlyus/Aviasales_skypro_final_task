from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class MyPage:
    BASE_URL = "https://www.aviasales.ru/"

    INPUT_DESTIN = (By.ID, "avia_form_destination-input")

    ORIRGIN_INPUT = (By.ID, "avia_form_origin-input")

    TICKET_INFORMATION = (By.XPATH, '//div[@class="s__vXk8zfZ14N8wleOX"]')

    DROPDOWN = (By.XPATH, "// ul[ @ id = 'avia_form_destination-menu']")

    DESTIN_ALERT = (
        By.XPATH,
        "//div[@data-test-id='text' and " + "text()='Укажите город прибытия']",
    )

    DATE_FORM_ALERT = (
        By.XPATH,
        "//div[@data-test-id='text' and text()='Укажите дату']",
    )

    START_DATE = (By.XPATH, '//button[@data-test-id="start-date-field"]')

    CALENDAR = (By.XPATH, '//div[@data-multiple-months="true"]')

    CHECKBOX = (By.CSS_SELECTOR, '[data-test-id="checkbox"]')

    SEARCH = (By.CSS_SELECTOR, '[type="button"][data-test-id="form-submit"]')

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_my_page(self):
        # Открывает страницу
        self.driver.set_page_load_timeout(15)
        try:
            # Пытаемся загрузить страницу
            self.driver.get(self.BASE_URL)
        except TimeoutException:

            self.driver.execute_script("window.stop();")

        self.wait.until(EC.presence_of_element_located(self.INPUT_DESTIN))

    def destination_click(self):
        # Нажимает на поле города назначения
        self.wait.until(
            EC.presence_of_element_located(self.INPUT_DESTIN)
        ).click()

    def input_to_origin_city(self, sity):
        # Вводит название города "Откуда"
        origin_city = self.wait.until(
            EC.presence_of_element_located(self.ORIRGIN_INPUT)
        )
        # Очищаем поле ввода
        origin_city.clear()
        # Вводим название
        origin_city.send_keys(sity)
        self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f'//span[@data-test-id="text"]'
                    f'//span[contains(text(), "{sity}")]',
                )
            )
        ).click()

    def input_to_destination(self, sity):
        # Вводит название города "Куда"
        destination = self.wait.until(
            EC.presence_of_element_located(self.INPUT_DESTIN)
        )
        # Очищаем поле ввода
        destination.clear()
        # Вводим название
        destination.send_keys(sity)
        try:
            # Пытаемся найти TICKET_INFORMATION
            self.wait.until(
                EC.presence_of_element_located(self.TICKET_INFORMATION)
            )
            # Если нашли, значит город уже выбран, ничего не делаем
        except TimeoutException:
            # Если TICKET_INFORMATION нет, выбрать город из выпадающего списка
            self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        f'//span[@data-test-id="text"]'
                        f'//span[contains(text(), "{sity}")]',
                    )
                )
            ).click()

            # После клика ждем появления информации о маршруте
            self.wait.until(
                EC.presence_of_element_located(self.TICKET_INFORMATION)
            )

    def is_dropdown(self):
        # Проверяет наличие dropdown на странице
        try:
            self.wait.until(EC.presence_of_element_located(self.DROPDOWN))
            return True
        except Exception as e:
            print(f"Dropdown не найден: {e}")
            return False

    def is_alert_destination(self):
        # Проверяет наличие ошибки: отсутствие города назначения
        try:
            self.wait.until(EC.presence_of_element_located(self.DESTIN_ALERT))
            return True
        except Exception as e:
            print(f"Alert город назначения не найден: {e}")
            return False

    def is_alert_date_form(self):
        # Проверяет наличие ошибки: отсутствие даты вылета
        try:
            self.wait.until(
                EC.presence_of_element_located(self.DATE_FORM_ALERT)
            )
            return True
        except Exception as e:
            print(f"Alert не найден: {e}")
            return False

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
        value = origin_input.get_attribute("value")
        print(f"Город отправления: {value}")
        return value

    def get_ticket_information(self, origin_city, destination_city):
        # Возвращает информацию о маршруте
        return self.wait.until(
            EC.presence_of_element_located(self.TICKET_INFORMATION)
        ).text

    def click_date(self, date):
        # Нажимает на кнопку с введённой датой
        date_element = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f'//div[@data-test-id="date-{date}"]')
            )
        )
        try:
            date_element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", date_element)

    def click_checkbox(self):
        # Нажимает на чекбокс Островка
        self.wait.until(EC.presence_of_element_located(self.CHECKBOX)).click()

    def click_search(self):
        # Нажимает поиск
        self.wait.until(EC.presence_of_element_located(self.SEARCH)).click()

    def result_search(self):
        # Проверяет успешность поиска
        # Проверяет, что URL изменился и содержит search
        if "search" not in self.driver.current_url:
            print(f"URL не содержит search: {self.driver.current_url}")
            return False

        # Проверяет наличие результатов поиска
        success_selectors = [
            (By.XPATH, "//div[contains(text(), 'Цены на соседние даты')]"),
            (By.CSS_SELECTOR, ".ticket-card, [data-test-id='ticket-card']"),
            (By.XPATH, "//*[contains(text(), 'Сохранить поиск')]"),
        ]

        for selector in success_selectors:
            try:
                self.wait.until(EC.presence_of_element_located(selector))
                return True
            except TimeoutException:
                continue

        return False
