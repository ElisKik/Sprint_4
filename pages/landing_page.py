import allure

from selenium.webdriver.common.by import By

from data.urls import Urls
from pages.base_page import BasePage
from utils.assert_helper import AssertHelper

class LandingPage(BasePage):
    button_order = [By.XPATH, './/div[starts-with(@class, "Home_FinishButton")]/button']
    container_faq = [By.XPATH, './/div[starts-with(@class, "Home_FAQ")]']
    container_question = lambda self, text: [By.XPATH, f'.//div[contains(text(), "{text}")]']
    container_answer = [By.XPATH, f'./../../div/p']

    @allure.step('Клик на кнопку Заказать')
    def click_button_order(self):
        self.click_awaited(self.button_order)

    @allure.step('Скролл к FAQ')
    def scroll_to_faq(self):
        self.scroll_to(self.container_faq)

    @allure.step('Скролл к кнопке Заказать')
    def scroll_to_button_order(self):
        self.scroll_to(self.button_order)

    @allure.step('Клик на вопрос')
    def click_question(self, text: str):
        locator = self.container_question(text)
        self.click_awaited(locator)

    @allure.step('Клик на ответ')
    def check_answer(self, question_text: str, answer_text: str):
        question_locator = self.container_question(question_text)

        question_element = self.webdriver.find_element(*question_locator)
        answer_element = question_element.find_element(*self.container_answer)

        AssertHelper.string_contains(answer_text, answer_element.text)

    @allure.step('Проверка перехода на страницу нового заказа')
    def check_page_changed_on_button_order(self):
        AssertHelper.current_url_is(self.webdriver, Urls.ORDER)

