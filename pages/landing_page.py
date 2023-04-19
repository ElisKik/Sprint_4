import allure

from selenium.webdriver import Firefox as WebDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.assert_messages import EqualityMismatch
from data.urls import Urls

class LandingPage:
    button_order = [By.XPATH, './/div[starts-with(@class, "Home_FinishButton")]/button']
    container_faq = [By.XPATH, './/div[starts-with(@class, "Home_FAQ")]']
    container_question = lambda self, text: [By.XPATH, f'.//div[contains(text(), "{text}")]']
    container_answer = [By.XPATH, f'./../../div/p']

    def __init__(self, webdriver: WebDriver, wait: WebDriverWait):
        self.webdriver = webdriver
        self.wait = wait

    @allure.step('Клик на кнопку Заказать')
    def click_button_order(self):
        element = self.webdriver.find_element(*self.button_order)
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step('Скролл к FAQ')
    def scroll_to_faq(self):
        element = self.webdriver.find_element(*self.container_faq)
        self.webdriver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Скролл к кнопке Заказать')
    def scroll_to_button_order(self):
        element = self.webdriver.find_element(*self.button_order)
        self.wait.until(EC.element_to_be_clickable(element))
        self.webdriver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Клик на вопрос')
    def click_question(self, text: str):
        locator = self.container_question(text)
        element = self.webdriver.find_element(*locator)

        self.wait.until(EC.element_to_be_clickable(element))

        element.click()

    @allure.step('Клик на ответ')
    def check_answer(self, question_text: str, answer_text: str):
        question_locator = self.container_question(question_text)

        question_element = self.webdriver.find_element(*question_locator)
        answer_element = question_element.find_element(*self.container_answer)

        assert answer_text in answer_element.text, EqualityMismatch.contains(answer_text, answer_element.text)

    @allure.step('Проверка перехода на страницу нового заказа')
    def check_page_changed_on_button_order(self):
        EqualityMismatch.to_current_url(self.webdriver, Urls.ORDER)

