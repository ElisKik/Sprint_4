import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from utils.random import RandomData

class OrderRentPage(BasePage):
    button_order = [By.XPATH, './/div[starts-with(@class, "Order_Buttons")]/button[text() = "Заказать"]']
    input_date = [By.XPATH, './/input[starts-with(@class, "Input_Input") and contains(@placeholder, "Когда привезти самокат")]']
    container_duration = [By.XPATH, './/div[contains(text(), "Срок аренды")]']
    container_duration_option = [By.CLASS_NAME, 'Dropdown-option']
    label_color = [By.XPATH, './/label[starts-with(@class, "Checkbox_Label")]']
    input_comment = [By.XPATH, './/input[starts-with(@class, "Input_Input") and contains(@placeholder, "Комментарий для курьера")]']
    container_confirmation = [By.XPATH, './/div[contains(text(), "Хотите оформить")]']

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
        self.send_keys(self.input_date, value)
        self.send_keys(self.input_date, Keys.ENTER)

    @allure.step('Ввод информации об аренде: срок аренды')
    def set_random_duration(self):
        self.click(self.container_duration)
        self.click_random(self.container_duration_option)

    @allure.step('Ввод информации об аренде: цвет самоката')
    def set_random_color(self):
        self.click_random(self.label_color)

    @allure.step('Ввод информации об аренде: комментарий')
    def set_comment(self, value: str):
        self.send_keys(self.input_comment, value)

    @allure.step('Ввод информации об аренде: отправка заказа')
    def click_button_order(self):
        self.click(self.button_order)

    @allure.step('Проверка успешного перехода к подтверждению заказа')
    def check_form_submitted(self):
        is_valid = len(self.webdriver.find_elements(*self.container_confirmation)) > 0
        assert is_valid, 'Order confirmation dialog was not found'

