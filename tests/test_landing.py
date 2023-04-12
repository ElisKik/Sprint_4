import allure

from selenium.webdriver import Firefox as WebDriver

from selenium.webdriver.support.wait import WebDriverWait

from data.urls import Urls
from pages.base_page import BasePage
from pages.landing_page import LandingPage

class TestLanding:

    @allure.title('Тест перехода с клика в лендинге на кнопку Заказать')
    @allure.description('Кликаем на кнопку **Заказать**, и проверяем \
                        что произошёл переход на страницу начала заказа')
    @allure.link(Urls.ORDER, name='Ожидаемый URL, на который должно произойти перенаправление')
    def test_click_button_order(self, webdriver: WebDriver, wait: WebDriverWait):
        base_page = BasePage(webdriver, wait)
        base_page.click_button_accept_cookies()

        landing_page = LandingPage(webdriver, wait)

        landing_page.click_button_order()
        landing_page.check_page_changed_on_button_order()

    @allure.title('Тест FAQ: вопрос о цене')
    @allure.description('Кликаем на вопрос и проверяем, что соседний элемент содержит ожидаемый ответ')
    def test_faq_price(self, webdriver: WebDriver, wait: WebDriverWait):
        base_page = BasePage(webdriver, wait)
        base_page.click_button_accept_cookies()

        landing_page = LandingPage(webdriver, wait)

        landing_page.scroll_to_faq()

        landing_page.click_question_faq_price()
        landing_page.check_answer_faq_price()

    @allure.title('Тест FAQ: вопрос о нескольких самокатах')
    @allure.description('Кликаем на вопрос и проверяем, что соседний элемент содержит ожидаемый ответ')
    def test_faq_multiple_scooters(self, webdriver: WebDriver, wait: WebDriverWait):
        base_page = BasePage(webdriver, wait)
        base_page.click_button_accept_cookies()

        landing_page = LandingPage(webdriver, wait)

        landing_page.scroll_to_faq()

        landing_page.click_question_faq_multiple_scooters()
        landing_page.check_answer_faq_multiple_scooters()

    @allure.title('Тест FAQ: вопрос о времени аренды')
    @allure.description('Кликаем на вопрос и проверяем, что соседний элемент содержит ожидаемый ответ')
    def test_faq_rent_rime(self, webdriver: WebDriver, wait: WebDriverWait):
        base_page = BasePage(webdriver, wait)
        base_page.click_button_accept_cookies()

        landing_page = LandingPage(webdriver, wait)

        landing_page.scroll_to_faq()

        landing_page.click_question_faq_rent_rime()
        landing_page.check_answer_faq_rent_time()

    @allure.title('Тест FAQ: вопрос об аренде сегодня')
    @allure.description('Кликаем на вопрос и проверяем, что соседний элемент содержит ожидаемый ответ')
    def test_faq_today(self, webdriver: WebDriver, wait: WebDriverWait):
        base_page = BasePage(webdriver, wait)
        base_page.click_button_accept_cookies()

        landing_page = LandingPage(webdriver, wait)

        landing_page.scroll_to_faq()

        landing_page.click_question_faq_today()
        landing_page.check_answer_faq_today()

    @allure.title('Тест FAQ: вопрос об изменениях срока аренды')
    @allure.description('Кликаем на вопрос и проверяем, что соседний элемент содержит ожидаемый ответ')
    def test_faq_change_terms(self, webdriver: WebDriver, wait: WebDriverWait):
        base_page = BasePage(webdriver, wait)
        base_page.click_button_accept_cookies()

        landing_page = LandingPage(webdriver, wait)

        landing_page.scroll_to_faq()

        landing_page.click_question_change_terms()
        landing_page.check_answer_faq_change_terms()
