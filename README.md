# Проект разработка Healthy_habit трекер полезных привычек


## Описание:
Проект разработка Healthy_habit трекер полезных привычек это домашнее задание студента


## Установка:
1. Клонируйте репозиторий 
``` git clone nttps:https://github.com/elenapantsurkina/Healthy_habit```


## Зависимости
- python 3.12
- django 5.1.1
- djangorestframework 3.15.2
- python-dotenv 1.0.1
- psycopg2-binary 2.9.10
- djangorestframework-simplejwt 5.4.0
- django-filter 24.3
- drf-yasg 1.21.8
- requests 2.32.3
- celery 5.4.0
- django-celery-beat 2.7.0
- redis 5.2.1
- django-cors-headers 4.6.0


## Установка зависимостей
```pip install django```
создайте файл .env и укажите там переменные: SECRET_KEY, NAME,USER_NAME,PASSWORD,HOST, 
CELERY_BROKER_URL,CELERY_RESULT_BACKEND, TELEGRAM_TOKEN.

## Конфигурация
Перед запуском проекта убедитесь, что все зависимости установлены и выполнены необходимые конфигурационные шаги


## Использование:
Для запуска проекта с использованием Docker Compose выполните следующую команду: 'docker-compose up --build'
Для развертывания проекта на сервере клонируйте репозиторий
Установите git и docker
Перенесите из .env все параметры в секреты. 
Также добавьте : DOCKER_HUB_ACCESS_TOKEN,DOCKER_HUB_USERNAME, SERVER_IP, SSH_KEY, SSH_USER
Запушьте любой коммит.

Для проверки работы приложения на localhost выполните команду `python manage.py runserver`


## Функционал:
Созданы приложения "habit" и "users".
Подключена БД.
В приложении users создана модель User. Авторизация по email.
В приложении habit созданf моделm Habit.
В приложении habit реализована валидация. 
Реализована CRUD для модели Habit с помощью Viewsets.
Реализованы сериализаторы.
Реализован CRUD для пользователей.
Настроено использование JWT-авторизации.
Определены права доступа.
Реализована пагинация .
Функционал работы приложений покрыты тестами.
Подключена и настроена вывод документации для проекта.
Подключены celery и celery-beat.
Настроена интеграцию с Телеграмом.
Настроена CORS..


## Документация:
отсутствует


## Лицензия 
Этот проект лицензирован под лицензией MIT. 