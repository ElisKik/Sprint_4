import allure

from typing import List

from selenium.webdriver import Firefox as WebDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class OrderCustomerPage:
    button_next = [By.XPATH, './/div[starts-with(@class, "Order_NextButton")]/button']
    input_first_name = [By.XPATH, './/input[starts-with(@class, "Input_Input") and contains(@placeholder, "Имя")]']
    input_last_name = [By.XPATH, './/input[starts-with(@class, "Input_Input") and contains(@placeholder, "Фамилия")]']
    input_address = [By.XPATH, './/input[starts-with(@class, "Input_Input") and contains(@placeholder, "Адрес")]']
    input_phone = [By.XPATH, './/input[starts-with(@class, "Input_Input") and contains(@placeholder, "Телефон")]']
    input_metro = [By.CLASS_NAME, 'select-search__input']
    container_metro_station = [By.XPATH, './/div[starts-with(@class, "Order_Text__")]']
    container_next_form = [By.XPATH, './/div[text()="Про аренду"]']

    def __init__(self, webdriver: WebDriver, wait: WebDriverWait):
        self.webdriver = webdriver
        self.wait = wait

    @allure.step('Ввод информации о заказчике: имя')
    def set_first_name(self, value: str):
        self.webdriver.find_element(*self.input_first_name).send_keys(value)

    @allure.step('Ввод информации о заказчике: фамилия')
    def set_last_name(self, value: str):
        self.webdriver.find_element(*self.input_last_name).send_keys(value)

    @allure.step('Ввод информации о заказчике: адрес')
    def set_address(self, value: str):
        self.webdriver.find_element(*self.input_address).send_keys(value)

    @allure.step('Ввод информации о заказчике: станция метро')
    def set_metro_station(self, value: str):
        self.webdriver.find_element(*self.input_metro).click()

        station_elements = self.webdriver.find_elements(*self.container_metro_station)
        my_station_element = next((station_element for station_element in station_elements if station_element.text == value), None)

        self.webdriver.execute_script("arguments[0].scrollIntoView();", my_station_element)

        assert my_station_element is not None, f'Element with text {value} was not found'

        my_station_element.click()

    @allure.step('Ввод информации о заказчике: номер телефона')
    def set_phone(self, value: str):
        self.webdriver.find_element(*self.input_phone).send_keys(value)

    @allure.step('Ввод информации о заказчике: клик на кнопку перехода к следующей форме')
    def click_button_next(self):
        self.webdriver.find_element(*self.button_next).click()

    @allure.step('Проверка валидности ввода: имя')
    def check_valid_first_name(self):
        self.__check_valid_input(self.input_first_name)

    @allure.step('Проверка валидности ввода: фамилия')
    def check_valid_last_name(self):
        self.__check_valid_input(self.input_last_name)

    @allure.step('Проверка валидности ввода: адрес')
    def check_valid_address(self):
        self.__check_valid_input(self.input_address)

    @allure.step('Проверка валидности ввода: номер телефона')
    def check_valid_phone(self):
        self.__check_valid_input(self.input_phone)

    @allure.step('Проверка успешного перехода к следующей форме оформления заказа')
    def check_form_switched(self):
        self.wait.until(lambda driver: len(driver.find_elements(*self.button_next)) == 0)
        assert len(self.webdriver.find_elements(*self.container_next_form)) > 0, f'Form was not switched to the next'

    def __check_valid_input(self, locator: List[str]):
        input_element = self.webdriver.find_element(*locator)

        given_value = input_element.get_attribute('value')

        input_element.clear()
        input_element.send_keys(given_value)

        error_locator = [By.XPATH, f'{locator[1]}/../div']

        error_element = self.webdriver.find_element(*error_locator)

        is_valid = len(error_element.text) == 0

        if not is_valid:
            allure.attach(
                body=self.webdriver.get_screenshot_as_png(),
                name='form-customer-input-validation-error',
                attachment_type=allure.attachment_type.PNG)

        assert is_valid, f'Input \'{given_value}\' is invalid: {error_element.text}'
