# Sprint_6 — автотесты «Яндекс.Самокат»

UI-автотесты для учебного сервиса [qa-scooter.praktikum-services.ru](https://qa-scooter.praktikum-services.ru/).
Selenium + pytest + Page Object Model + Allure.

## Что покрыто тестами

- **Раздел «Вопросы о важном»** — каждый из 8 вопросов раскрывается и показывает верный ответ (параметризация)
- **Заказ самоката** — позитивный сценарий с двумя наборами данных и двумя точками входа: кнопка «Заказать» вверху и внизу страницы
- **Навигация по логотипам** — переход на главную по логотипу «Самоката», открытие Дзена в новом окне по логотипу Яндекса

## Структура проекта
Sprint_6/
├── pages/ # Page Object
│ ├── base_page.py # общие методы: ожидания, клики, ввод текста
│ ├── main_page.py # главная страница: FAQ, кнопки заказа, логотипы
│ └── order_page.py # форма заказа: два шага + модальные окна
├── tests/
│ ├── test_faq.py
│ ├── test_order.py
│ └── test_navigation.py
├── conftest.py # фикстура driver (Firefox)
├── data.py # URL, тестовые данные, тексты FAQ
└── requirements.txt


## Установка

```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Понадобится браузер **Mozilla Firefox** — Selenium 4 сам подтянет geckodriver через Selenium Manager, отдельно ставить его не нужно.

## Запуск тестов

```bash
python3 -m pytest -v
```

Запуск отдельного файла:

```bash
python3 -m pytest tests/test_order.py -v
```

## Allure-отчёт

```bash
python3 -m pytest --alluredir=allure_results --clean-alluredir
allure generate allure_results -o allure-report --clean
allure open allure-report
```

Установка Allure CLI (если ещё не стоит): `brew install allure` (macOS).

## Где использована параметризация

- `test_faq.py` — один тест прогоняется на 8 наборах `(индекс, вопрос, ответ)`, то есть каждый вопрос проверяется отдельным кейсом
- `test_order.py` — один тест на два набора `(точка входа, данные заказа)`: верхняя кнопка «Заказать» с первым набором данных, нижняя — со вторым, без дублирования сценария