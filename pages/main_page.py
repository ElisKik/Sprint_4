import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from data.urls import Urls
from pages.base_page import BasePage
from utils.assert_helper import AssertHelper

class MainPage(BasePage):
    logo_yandex = [By.XPATH, './/a[starts-with(@class, "Header_LogoYandex")]']
    logo_scooter = [By.XPATH, './/a[starts-with(@class, "Header_LogoScooter")]']
    button_order = [By.XPATH, './/div[starts-with(@class, "Header_Nav")]/button[starts-with(@class, "Button_Button")]']
    button_status = [By.XPATH, './/div[starts-with(@class, "Header_Nav")]/button[starts-with(@class, "Header_Link")]']
    input_search_order = [By.XPATH, './/div[starts-with(@class, "Header_SearchInput")]/div/input']
    button_search_order = [By.XPATH, './/div[starts-with(@class, "Header_SearchInput")]/button']

    @allure.step('Клик на лого Яндекса')
    def click_logo_yandex(self):
        self.click(self.logo_yandex)

    @allure.step('Клик на лого Яндекс.Самокат')
    def click_logo_scooter(self):
        self.click(self.logo_scooter)

    @allure.step('Клик на кнопку Заказать')
    def click_button_order(self):
        self.click(self.button_order)

    @allure.step('Клик на кнопку Статус заказа')
    def click_button_status(self):
        self.click(self.button_status)

    @allure.step('Ввод ID заказа')
    def set_order_id(self, value: str):
        self.send_keys(self.input_search_order, value)

    @allure.step('Клик на кнопку поиска заказа по ID')
    def click_button_search_order(self):
        self.click(self.button_search_order)

    @allure.step('Проверка перенаправления на главную страницу Яндекса')
    def check_redirected_from_logo_yandex(self):
        self.wait_url_to_be_in_any_window(Urls.YANDEX_BASE)
        AssertHelper.current_url_is(self.webdriver, Urls.YANDEX_BASE)

    @allure.step('Проверка перенаправления на главную страницу Яндекс.Самокат')
    def check_redirected_from_logo_scooter(self):
        AssertHelper.current_url_is(self.webdriver, Urls.BASE)

    @allure.step('Проверка перехода на страницу нового заказа')
    def check_page_changed_on_button_order(self):
        AssertHelper.current_url_is(self.webdriver, Urls.ORDER)

    @allure.step('Проверка появления поля ввода для поиска существующего заказа')
    def check_input_appeared_on_button_status(self):
        locator = self.input_search_order
        self.wait.until(EC.visibility_of_element_located(locator))
        AssertHelper.is_displayed(self.webdriver, locator)

