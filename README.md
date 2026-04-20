<h1 align="center">
  🚀 Привет, я Дмитрий<br>
  🧪 QA Automation Engineer<br>
  🐍 Python разработчик<br>
  ⚡ API + UI тестирование
</h1>

<h3 align="center">
  👨‍💻 QA Automation Engineer | Python | Selenium | API Testing
</h3>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=1DimonNT&style=flat-square&color=blue" />
</p>

---

## 🎓 Обо мне

Я закончил **Уральский Государственный Педагогический Университет**

**Специальность:** Предприниматель-технолог

Затем прошел обучение в **QA.GURU**

**Курс:** [Инженер по автоматизации тестирования на Python](https://qa.guru/python)

---

## 🛠 Навыки

| Категория | Технологии |
|-----------|------------|
| **API** | REST API, JSON, Postman, Requests |
| **UI** | Selenium, Page Object |
| **CI/CD** | Jenkins, GitHub Actions |
| **Отчетность** | Allure (скриншоты, логи, видео) |
| **Контейнеризация** | Selenoid, Docker |
| **Архитектура** | YAGNI, KISS, SOLID, DRY |
| **VCS** | Git, GitHub |
| **Веб-разработка** | HTML5, CSS3, SEO, Schema.org |

---

## 📦 Что я умею

- ✅ Создавать тестовые проекты с нуля
- ✅ Строить архитектуру автотестов (Page Object)
- ✅ Тестировать API (Requests + Allure)
- ✅ Создавать UI-автотесты (Selenium)
- ✅ Настраивать CI/CD в Jenkins
- ✅ Генерировать Allure отчеты с вложениями
- ✅ Отправлять уведомления в Telegram
- ✅ Создавать и настраивать сайты (HTML, CSS, SEO)

---

## 🔧 Инструменты

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" />
  <img src="https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white" />
  <img src="https://img.shields.io/badge/Allure-000000?style=for-the-badge&logo=allure&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
</p>

---

## 📁 Проект 1: Test Automation Framework

Демонстрационный проект, показывающий навыки автоматизации тестирования. Фреймворк покрывает **UI** и **API** тесты с подробными Allure-отчётами.

### 🏗️ Архитектура проекта

```text
Python_portfolio/
├── config/
│   ├── settings.py
│   └── __init__.py
├── models/
│   └── user.py
├── pages/
│   └── registration_page.py
├── tests/
│   ├── api/
│   │   └── test_reqres.py
│   └── ui/
│       ├── test_registration.py
│       └── test_registration_demoqa.py
├── utils/
│   └── attach.py
├── .env
├── pytest.ini
├── requirements.txt
└── README.md
```
### ✅ Тестовое покрытие

#### 🌐 UI Тесты

| Сайт | Сценарий | Статус |
|------|----------|--------|
| SauceDemo | Успешный логин | ✅ |
| DemoQA | Регистрация студента | ✅ |

#### 🔌 API Тесты (JSONPlaceholder)

| Метод | Эндпоинт | Статус |
|-------|----------|--------|
| GET | /posts | ✅ |
| POST | /posts | ✅ |
| PUT | /posts/{id} | ✅ |
| DELETE | /posts/{id} | ✅ |
## 🚀 Запуск проекта

### 1. Клонирование и установка

```bash
git clone https://github.com/1DimonNT/Python_portfolio.git
cd Python_portfolio
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
### 2. Настройка окружения
Создайте файл .env:
```
SELENOID_URL=ru.selenoid.autotests.cloud/wd/hub
SELENOID_USER=user1
SELENOID_PASSWORD=1234
BASE_URL=https://demoqa.com
API_BASE_URL=https://reqres.in/api
BROWSER=chrome
BROWSER_VERSION=128.0
WINDOW_SIZE=1920,1080
TIMEOUT=30
```
### 3. Запуск тестов
``` 
pytest --alluredir=allure-results -v
```
### 4. Просмотр Allure-отчёта
```
allure serve allure-results
```
## 📊 Отчётность

### Что входит в Allure-отчёт:

| Компонент | Описание |
|-----------|----------|
| 📸 Скриншоты | Финальное состояние страницы после теста |
| 🎬 Видео | Полная запись выполнения теста (Selenoid) |
| 📄 HTML | Page Source для отладки |
| 📋 Логи | Консольные логи браузера |

## 📈 Результаты

| Показатель | Значение |
|------------|----------|
| Всего тестов | 6 |
| UI тестов | 2 |
| API тестов | 4 |
| Проходимость | 100% ✅ |
###  🌐 Проект 2: Сайт "Центр Чистоты НТ"
Этот сайт я полностью разработал и настроил самостоятельно — от идеи до публикации.
```
🔗 Ссылка: github.com/1DimonNT/center-chistoty-nt.ru
```
### 🛠 Что сделано мной:

| Задача | Реализация |
|--------|------------|
| Вёрстка | Полностью адаптивная, семантическая HTML5/CSS3 |
| Дизайн | Самостоятельно, без фреймворков |
| SEO | Микроразметка Schema.org, уникальные мета-теги |
| Оптимизация | WebP, lazy loading, минимизация CSS/JS |
| Формы | Умная форма заказа с копированием в буфер |
| Аналитика | Настроил Yandex.Metrika |
| Хостинг | Настроил GitHub Pages + кастомный домен |
| Видео | Интеграция Rutube через iframe |

### 📋 Услуги на сайте

- 🧼 Химчистка мебели
- 🐜 Дезинсекция
- 🧹 Клининг
- 💨 Озонация
- 🕷️ Акарицидная обработка

## 📫 Контакты
<p align="center"> <a href="https://github.com/1DimonNT"><img src="https://img.shields.io/badge/GitHub-1DimonNT-181717?style=for-the-badge&logo=github" /></a> <a href="https://t.me/Ivantsov_Dima"><img src="https://img.shields.io/badge/Telegram-@Ivantsov_Dima-26A5E4?style=for-the-badge&logo=telegram" /></a> <a href="https://vk.com/id4666416"><img src="https://img.shields.io/badge/VK-@id4666416-0077FF?style=for-the-badge&logo=vk&logoColor=white" /></a> <a href="mailto:1DimonNT@gmail.com"><img src="https://img.shields.io/badge/Email-1DimonNT%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" /></a> </p>
*© 2025 Дмитрий Иванцов*


