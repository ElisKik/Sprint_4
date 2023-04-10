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

Coming soon.
