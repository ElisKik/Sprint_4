# Тесты сайта **Яндекс.Самокат**

В этом репозитории будут представлены UI-тесты функциональности сайта [**Яндекс.Самокат**](https://qa-scooter.praktikum-services.ru/).

## Стек технологий

- **Python 3.10**
- **PyTest**
- **Selenium**
- **Allure**

## Как запустить

1. Открыть терминал.
2. Склонировать репозиторий.
3. Перейти в директорию репозитория с помощью команды `cd`
4. Развернуть virtual environment:

   ```bash
   python -m venv .venv
   ```

5. Запустить virtual environment:

   - MacOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

   - Windows

     ```bash
     .venv\Scripts\activate
     ```

6. Установить зависимости внутри virtual environment:

   ```bash
   pip install -r requirements.txt
   ```

7. Запустить тесты:

   ```bash
   pytest -v tests --alluredir=allure_results
   ```

8. Посмотреть отчёт о тестировании через **Allure**.

   ```bash
   allure serve allure_results
   ```

## Реализованные тесты

- [*] Тест перенаправления с клика на логотип Яндекса
- [*] Тест перехода с клика на логотип Яндекс.Самокат
- [*] Тест появления поля поиска заказа с клика на кнопку **Статус заказа**
- [*] Тест FAQ: вопрос об аренде сегодня
- [*] Тест FAQ: вопрос об доставке в область
- [*] Тест FAQ: вопрос об изменениях срока аренды
- [*] Тест FAQ: вопрос об отмене заказа
- [*] Тест FAQ: вопрос о времени аренды
- [*] Тест FAQ: вопрос о зарядке
- [*] Тест FAQ: вопрос о нескольких самокатах
- [*] Тест FAQ: вопрос о цене
- [*] Тест перехода с клика в лендинге на кнопку **Заказать**
- [*] Тест перехода с клика в хэдере на кнопку **Заказать**
- [*] Тест подтверждения отправки нового заказа с лендинга
- [*] Тест неподтверждения отправки нового заказа с лендинга
- [*] Тест подтверждения отправки нового заказа с хэдера
- [*] Тест неподтверждения отправки нового заказа с хэдера
- [*] Тест получения статуса заказа со страницы успешного завершения оформления заказа
- [*] Тест получения статуса заказа с поля поиска в хэдере
