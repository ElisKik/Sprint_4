import allure

from random import choice

from selenium.webdriver import Firefox as WebDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils.random import RandomData

class OrderRentPage:
    button_order = [By.XPATH, './/div[starts-with(@class, "Order_Buttons")]/button[text() = "Заказать"]']
    input_date = [By.XPATH, './/input[starts-with(@class, "Input_Input") and contains(@placeholder, "Когда привезти самокат")]']
    container_duration = [By.XPATH, './/div[contains(text(), "Срок аренды")]']
    container_duration_option = [By.CLASS_NAME, 'Dropdown-option']
    label_color = [By.XPATH, './/label[starts-with(@class, "Checkbox_Label")]']
    input_comment = [By.XPATH, './/input[starts-with(@class, "Input_Input") and contains(@placeholder, "Комментарий для курьера")]']
    container_confirmation = [By.XPATH, './/div[contains(text(), "Хотите оформить")]']

    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver

    @allure.step('Заполнение информации об аренде')
    def fill_form(self):
        date_string = RandomData.get_date_string()
        self.set_date(date_string)

        self.set_random_duration()
        self.set_random_color()

        comment = RandomData.get_text()
        self.set_comment(comment)

        self.click_button_order()
        self.check_form_submitted()

    @allure.step('Ввод информации об аренде: дата')
    def set_date(self, value: str):
        element = self.webdriver.find_element(*self.input_date)
        element.send_keys(value)
        element.send_keys(Keys.ENTER)

    @allure.step('Ввод информации об аренде: срок аренды')
    def set_random_duration(self):
        self.webdriver.find_element(*self.container_duration).click()

        duration_elements = self.webdriver.find_elements(*self.container_duration_option)

        duration_element = choice(duration_elements)

        self.webdriver.execute_script("arguments[0].scrollIntoView();", duration_element)

        duration_element.click()

    @allure.step('Ввод информации об аренде: цвет самоката')
    def set_random_color(self):
        color_elements = self.webdriver.find_elements(*self.label_color)

        color_element = choice(color_elements)
        color_element.click()

    @allure.step('Ввод информации об аренде: комментарий')
    def set_comment(self, value: str):
        element = self.webdriver.find_element(*self.input_comment)
        element.send_keys(value)

    @allure.step('Ввод информации об аренде: отправка заказа')
    def click_button_order(self):
        element = self.webdriver.find_element(*self.button_order)
        element.click()

    @allure.step('Проверка успешного перехода к подтверждению заказа')
    def check_form_submitted(self):
        is_valid = len(self.webdriver.find_elements(*self.container_confirmation)) > 0
        assert is_valid, 'Order confirmation dialog was not found'

