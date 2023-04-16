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
    container_faq_price_question = [By.XPATH, './/div[contains(text(), "Сколько это стоит")]']
    container_faq_multiple_scooters_question = [By.XPATH, './/div[contains(text(), "несколько самокатов")]']
    container_faq_rent_time_question = [By.XPATH, './/div[contains(text(), "рассчитывается время аренды")]']
    container_faq_today_question = [By.XPATH, './/div[contains(text(), "прямо на сегодня")]']
    container_faq_change_terms_question = [By.XPATH, './/div[contains(text(), "продлить заказ")]']
    container_faq_charging_question = [By.XPATH, './/div[contains(text(), "привозите зарядку")]']
    container_faq_cancel_question = [By.XPATH, './/div[contains(text(), "отменить заказ")]']
    container_faq_delivery_question = [By.XPATH, './/div[contains(text(), "за МКАДом")]']

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

    @allure.step('Клик в FAQ по вопросу о цене')
    def click_question_faq_price(self):
        element = self.webdriver.find_element(*self.container_faq_price_question)
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step('Клик в FAQ по вопросу о нескольких самокатах')
    def click_question_faq_multiple_scooters(self):
        element = self.webdriver.find_element(*self.container_faq_multiple_scooters_question)
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step('Клик в FAQ по вопросу о времени аренды')
    def click_question_faq_rent_rime(self):
        element = self.webdriver.find_element(*self.container_faq_rent_time_question)
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step('Клик в FAQ по вопросу об аренде сегодня')
    def click_question_faq_today(self):
        element = self.webdriver.find_element(*self.container_faq_today_question)
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step('Клик в FAQ по вопросу об изменениях срока аренды')
    def click_question_faq_change_terms(self):
        element = self.webdriver.find_element(*self.container_faq_change_terms_question)
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step('Клик в FAQ по вопросу о зарядке')
    def click_question_faq_charging(self):
        element = self.webdriver.find_element(*self.container_faq_charging_question)
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step('Клик в FAQ по вопросу об отмене заказа')
    def click_question_faq_cancel(self):
        element = self.webdriver.find_element(*self.container_faq_cancel_question)
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step('Клик в FAQ по вопросу о доставке в область')
    def click_question_faq_delivery(self):
        element = self.webdriver.find_element(*self.container_faq_delivery_question)
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step('Проверка перехода на страницу нового заказа')
    def check_page_changed_on_button_order(self):
        expected = Urls.ORDER
        actual = self.webdriver.current_url

        assert expected == actual, EqualityMismatch.strings(expected, actual)

    @allure.step('Проверка ответа в FAQ на вопрос о цене')
    def check_answer_faq_price(self):
        answer_locator = [By.XPATH, f'{self.container_faq_price_question[1]}/../../div/p']
        element = self.webdriver.find_element(*answer_locator)

        expected_entry = '400 рублей'
        actual_text = element.text

        assert expected_entry in actual_text, EqualityMismatch.contains(expected_entry, actual_text)

    @allure.step('Проверка ответа в FAQ на вопрос о нескольких самокатах')
    def check_answer_faq_multiple_scooters(self):
        answer_locator = [By.XPATH, f'{self.container_faq_multiple_scooters_question[1]}/../../div/p']
        element = self.webdriver.find_element(*answer_locator)

        expected_entry = 'один заказ — один самокат'
        actual_text = element.text

        assert expected_entry in actual_text, EqualityMismatch.contains(expected_entry, actual_text)

    @allure.step('Проверка ответа в FAQ на вопрос о времени аренды')
    def check_answer_faq_rent_time(self):
        answer_locator = [By.XPATH, f'{self.container_faq_rent_time_question[1]}/../../div/p']
        element = self.webdriver.find_element(*answer_locator)

        expected_entry = 'начинается с момента'
        actual_text = element.text

        assert expected_entry in actual_text, EqualityMismatch.contains(expected_entry, actual_text)

    @allure.step('Проверка ответа в FAQ на вопрос об аренде сегодня')
    def check_answer_faq_today(self):
        answer_locator = [By.XPATH, f'{self.container_faq_today_question[1]}/../../div/p']
        element = self.webdriver.find_element(*answer_locator)

        expected_entry = 'начиная с завтрашнего дня'
        actual_text = element.text

        assert expected_entry in actual_text, EqualityMismatch.contains(expected_entry, actual_text)

    @allure.step('Проверка ответа в FAQ на вопрос об изменениях срока аренды')
    def check_answer_faq_change_terms(self):
        answer_locator = [By.XPATH, f'{self.container_faq_change_terms_question[1]}/../../div/p']
        element = self.webdriver.find_element(*answer_locator)

        expected_entry = 'если что-то срочное'
        actual_text = element.text

        assert expected_entry in actual_text, EqualityMismatch.contains(expected_entry, actual_text)

    @allure.step('Проверка ответа в FAQ на вопрос о зарядке')
    def check_answer_faq_charging(self):
        answer_locator = [By.XPATH, f'{self.container_faq_charging_question[1]}/../../div/p']
        element = self.webdriver.find_element(*answer_locator)

        expected_entry = 'Зарядка не понадобится'
        actual_text = element.text

        assert expected_entry in actual_text, EqualityMismatch.contains(expected_entry, actual_text)

    @allure.step('Проверка ответа в FAQ на вопрос об отмене заказа')
    def check_answer_faq_cancel(self):
        answer_locator = [By.XPATH, f'{self.container_faq_cancel_question[1]}/../../div/p']
        element = self.webdriver.find_element(*answer_locator)

        expected_entry = 'пока самокат не привезли'
        actual_text = element.text

        assert expected_entry in actual_text, EqualityMismatch.contains(expected_entry, actual_text)

    @allure.step('Проверка ответа в FAQ на вопрос о доставке в область')
    def check_answer_faq_delivery(self):
        answer_locator = [By.XPATH, f'{self.container_faq_delivery_question[1]}/../../div/p']
        element = self.webdriver.find_element(*answer_locator)

        expected_entry = 'И Москве, и Московской области'
        actual_text = element.text

        assert expected_entry in actual_text, EqualityMismatch.contains(expected_entry, actual_text)
