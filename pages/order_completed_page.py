from re import search

import allure

from selenium.webdriver import Firefox as WebDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class OrderCompletedPage:
    container_title = [By.XPATH, './/div[text() = "Заказ оформлен"]']
    container_caption = [By.XPATH, './/div[starts-with(@class, "Order_Text")]']
    button_status = [By.XPATH, './/div[starts-with(@class, "Order_NextButton")]/button']

    pattern_order_id = r':\s+([^.]+)'

    def __init__(self, webdriver: WebDriver, wait: WebDriverWait):
        self.webdriver = webdriver
        self.wait = wait

    @allure.step('Получение ID заказа')
    def get_order_id(self) -> str | None:
        element = self.webdriver.find_element(*self.container_caption)
        order_id_match = search(self.pattern_order_id, element.text)

        if order_id_match is not None:
            return order_id_match.group(1)

        return None

    @allure.step('Клик на кнопку Посмотреть статус')
    def click_button_status(self):
        element = self.webdriver.find_element(*self.button_status)
        element.click()

    @allure.step('Проверка присутствия ID заказа на странице')
    def check_has_order_id(self):
        element = self.webdriver.find_element(*self.container_caption)
        assert search(self.pattern_order_id, element.text) is not None, 'Order ID was not found'

