import allure
import pytest

from selenium.webdriver import Firefox as WebDriver

from data.urls import Urls
from pages.base_page import BasePage
from pages.landing_page import LandingPage

class TestLanding:
    @allure.title('Тест перехода с клика в лендинге на кнопку Заказать')
    @allure.description('Кликаем на кнопку **Заказать**, и проверяем \
                        что произошёл переход на страницу начала заказа')
    @allure.link(Urls.ORDER, name='Ожидаемый URL, на который должно произойти перенаправление')
    def test_click_button_order(self, webdriver: WebDriver):
        base_page = BasePage(webdriver)

        landing_page = LandingPage(webdriver, base_page)

        landing_page.scroll_to_button_order()

        landing_page.click_button_order()
        landing_page.check_page_changed_on_button_order()

    @allure.title('Тест FAQ')
    @allure.description('Кликаем на вопрос и проверяем, что соседний элемент содержит ожидаемый ответ')
    @pytest.mark.parametrize(
        'question, answer',
        [
            ('Сколько это стоит', '400 рублей'),
            ('несколько самокатов', 'один заказ — один самокат'),
            ('рассчитывается время аренды', 'начинается с момента'),
            ('прямо на сегодня', 'начиная с завтрашнего дня'),
            ('продлить заказ', 'если что-то срочное'),
            ('привозите зарядку', 'Зарядка не понадобится'),
            ('отменить заказ', 'пока самокат не привезли'),
            ('за МКАДом', 'И Москве, и Московской области'),
        ]
    )
    def test_faq(self, webdriver: WebDriver, question: str, answer: str):
        base_page = BasePage(webdriver)

        landing_page = LandingPage(webdriver, base_page)

        landing_page.scroll_to_faq()

        landing_page.click_question(question)
        landing_page.check_answer(question, answer)

