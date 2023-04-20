import allure

from random import choice
from typing import List

from selenium.webdriver import Firefox as WebDriver

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.random import RandomData

class OrderCustomerPage:
    button_next = [By.XPATH, './/div[starts-with(@class, "Order_NextButton")]/button']
    input_first_name = [By.XPATH, './/input[starts-with(@class, "Input_Input") and contains(@placeholder, "Имя")]']
    input_last_name = [By.XPATH, './/input[starts-with(@class, "Input_Input") and contains(@placeholder, "Фамилия")]']
    input_address = [By.XPATH, './/input[starts-with(@class, "Input_Input") and contains(@placeholder, "Адрес")]']
    input_phone = [By.XPATH, './/input[starts-with(@class, "Input_Input") and contains(@placeholder, "Телефон")]']
    input_metro = [By.CLASS_NAME, 'select-search__input']
    container_metro_station = [By.XPATH, './/div[starts-with(@class, "Order_Text__")]']
    container_next_form = [By.XPATH, './/div[text()="Про аренду"]']

    def __init__(self, webdriver: WebDriver, base_page: BasePage):
        self.webdriver = webdriver
        self.base_page = base_page

    @allure.step('Заполнение информации о заказчике')
    def fill_form(self):
        first_name, last_name = RandomData.get_name()

        self.set_first_name(first_name)
        self.check_valid_first_name()

        self.set_last_name(last_name)
        self.check_valid_last_name()

        address = RandomData.get_address()
        self.set_address(address)
        self.check_valid_address()

        self.set_random_metro_station()

        phone_number = RandomData.get_phone()
        self.set_phone(phone_number)
        self.check_valid_phone()

        self.click_button_next()
        self.check_form_switched()

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
    def set_random_metro_station(self):
        self.webdriver.find_element(*self.input_metro).click()

        station_elements = self.webdriver.find_elements(*self.container_metro_station)

        random_metro_station_element = choice(station_elements)

        self.webdriver.execute_script("arguments[0].scrollIntoView();", random_metro_station_element)

        random_metro_station_element.click()

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
        self.base_page.wait.until(lambda driver: len(driver.find_elements(*self.button_next)) == 0)
        assert len(self.webdriver.find_elements(*self.container_next_form)) > 0, f'Form was not switched to the next'

    def __check_valid_input(self, locator: List[str]):
        input_element = self.webdriver.find_element(*locator)

        given_value = input_element.get_attribute('value')

        input_element.clear()
        input_element.send_keys(given_value)

        error_locator = [By.XPATH, f'{locator[1]}/../div']

        error_element = self.webdriver.find_element(*error_locator)

        is_valid = len(error_element.text) == 0

        assert is_valid, f'Input \'{given_value}\' is invalid: {error_element.text}'

