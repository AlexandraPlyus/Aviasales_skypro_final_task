from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC


class MyPage:
    BASE_URL = "https://www.aviasales.ru/"

    INPUT_DESTIN = (By.ID, "avia_form_destination-input")

    DROPDOWN = (
        By.CSS_SELECTOR, '#avia_form_destination-item-0[data-test-id="text"]span')

    CHECKBOX = (
        By.CSS_SELECTOR, 'label[data-test-id="checkbox"] > input[type=checkbox]'
    )

    SEARCH = (By.CSS_SELECTOR, '[type="button"][data-test-id="form-submit"]')

    # START_DATE = (
    #     By.CSS_SELECTOR, '[data-test-id="start-date-value"][text()="Когда"]'
    # )

    # Отсутствие города прибытия (By.CSS_SELECTOR, '[data-test-id="text"][text()="Укажите город прибытия"]

    # Отсутствие даты вылета (By.CSS_SELECTOR, '[data-test-id="text"][text()="Укажите дату"]')

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_my_page(self):
        self.driver.get(self.BASE_URL)

        self.wait.until(
            EC.presence_of_element_located(self.INPUT_DESTIN)
        )

    def input_to_destination(self, sity):
        destination = self.wait.until(
            EC.presence_of_element_located(self.INPUT_DESTIN)
        )

        # Очищаем поле ввода
        destination.clear()
        # Вводим название
        destination.send_keys(sity)

        dropdown = self.wait.until(
            EC.presence_of_element_located(self.DROPDOWN)
        )
        return dropdown.text

    def click_checkbox(self):
        self.CHECKBOX.click()

    def click_search(self):
        self.SEARCH.click()

    # def input_to_start_date(self, start_date):
    #     self.START_DATE.send_keys(start_date)

    def empty_destin(self):
        self.INPUT_DESTIN.clear()
        
