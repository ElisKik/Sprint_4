import allure

from selenium.webdriver import Firefox as WebDriver

from selenium.webdriver.common.by import By

class OrderConfirmPage:
    button_yes = [By.XPATH, './/button[text() = "Да"]']
    button_no = [By.XPATH, './/button[text() = "Да"]']
    button_order = [By.XPATH, './/button[text() = "Заказать"]']
    container_order_made = [By.XPATH, './/div[text() = "Заказ оформлен"]']

    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver

    @allure.step('Клик на кнопку Да')
    def click_button_yes(self):
        element = self.webdriver.find_element(*self.button_yes)
        element.click()

    @allure.step('Клик на кнопку Нет')
    def click_button_no(self):
        element = self.webdriver.find_element(*self.button_yes)
        element.click()

    @allure.step('Проверка подтверждения заказа пользователем')
    def check_order_confirmed(self):
        is_valid = len(self.webdriver.find_elements(*self.container_order_made)) > 0
        assert is_valid, 'Dialog after order confirmation is not valid'

    @allure.step('Проверка неподтверждения заказа пользователем')
    def check_order_not_confirmed(self):
        is_valid = len(self.webdriver.find_elements(*self.button_order)) > 0
        assert is_valid, 'Previous form before order confirmation is not valid'

