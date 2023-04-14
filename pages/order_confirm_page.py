import allure

from selenium.webdriver import Firefox as WebDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class OrderConfirmPage:
    button_yes = [By.XPATH, './/button[text() = "Да"]']
    button_no = [By.XPATH, './/button[text() = "Да"]']
    button_order = [By.XPATH, './/button[text() = "Заказать"]']
    container_order_made = [By.XPATH, './/div[text() = "Заказ оформлен"]']

    def __init__(self, webdriver: WebDriver, wait: WebDriverWait):
        self.webdriver = webdriver
        self.wait = wait

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

        if not is_valid:
            allure.attach(
                body=self.webdriver.get_screenshot_as_png(),
                name='order-confirmation-yes-unexpected',
                attachment_type=allure.attachment_type.PNG)

        assert is_valid, 'Dialog after order confirmation is not valid'

    @allure.step('Проверка неподтверждения заказа пользователем')
    def check_order_not_confirmed(self):
        is_valid = len(self.webdriver.find_elements(*self.button_order)) > 0

        if not is_valid:
            allure.attach(
                body=self.webdriver.get_screenshot_as_png(),
                name='order-confirmation-no-unexpected',
                attachment_type=allure.attachment_type.PNG)

        assert is_valid, 'Previous form before order confirmation is not valid'
