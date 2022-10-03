# Проект «Продуктовый помощник»

![Foodgram workflow](https://github.com/aoamosova/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg?branch=master&event=push)

Cайт «Продуктовый помощник». Пользователи сервиса смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Аутентификация по токену - библиотека Djoser
Поддерживает методы GET, POST, PUT, PATCH, DELET
Предоставляет данные в формате JSON
## Стек технологий
- проект написан на Python с использованием Django REST Framework;
- библиотека Djoser - аутентификация токенами;
- библиотека django-filter - фильтрация запросов;
- базы данных - PostgreSQL
- автоматическое развертывание проекта - Docker, docker-compose
- система управления версиями - git
- настроен непрерывный процесс разработки, тестирования и деплоя кода на боевой сервер CI/CD

## Проект в интернете
Проект запущен и доступен по адресу [http://62.84.116.89/recipes](http://62.84.116.89/recipes)

Админка доступна по адресу [http://62.84.116.89/admin/](http://62.84.116.89/admin/)
*login: admin
*email: admin@inbox.ru
*pass: admin

Документация для написания api проекта доступна по адресу [http://62.84.116.89/api/docs/redoc.html](http://62.84.116.89/api/docs/redoc.html)

## Подготовка и запуск проекта
* Склонируйте репозиторий на локальную машину.

### Для работы с удаленным сервером (на ubuntu):
* Выполните вход на свой удаленный сервер.

* Установите docker на сервер:
```
sudo apt install docker.io 
```
* Установите docker-compose на сервер. [Установка и использование Docker Compose в Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-ru)
* Локально отредактируйте файл infra/nginx/default.conf.conf, в строке server_name впишите свой IP
* Скопируйте файлы docker-compose.yml и nginx.conf из папки infra на сервер:
```
scp infra/docker-compose.yml <username>@<ip host>:/home/<username>/docker-compose.yml
scp infra/nginx.conf <username>@<ip host>:/home/<username>/nginx.conf
```
* Для работы с Workflow добавьте в Secrets GitHub переменные окружения для работы:
    ```
    DB_ENGINE=<django.db.backends.postgresql>
    DB_NAME=<имя базы данных postgres>
    DB_USER=<пользователь бд>
    DB_PASSWORD=<пароль>
    DB_HOST=<db>
    DB_PORT=<5432>
    
    DOCKER_PASSWORD=<пароль от DockerHub>
    DOCKER_USERNAME=<имя пользователя на DockerHub>
    
    SECRET_KEY=<секретный ключ проекта django>

    USER=<username для подключения к серверу>
    HOST=<IP сервера>
    SSH_KEY=<ваш SSH ключ (для получения выполните команду: cat ~/.ssh/id_rsa)>
    PASSPHRASE=<если при создании ssh-ключа вы использовали фразу-пароль>

    TELEGRAM_TO=<ID чата, в который придет сообщение, узнать свой ID можно у бота @userinfobot>
    TELEGRAM_TOKEN=<токен вашего бота, получить этот токен можно у бота @BotFather>
    ```
* Workflow состоит из четырех шагов:
     - Проверка кода на соответствие PEP8 и выполнение тестов, реализованных в проекте
     - Сборка и публикация образа приложения на DockerHub.
     - Автоматическое скачивание образа приложения и деплой на удаленном сервере.
     - Отправка уведомления в телеграм-чат.  
  

* После успешного развертывания проекта на удаленном сервере, можно выполнить:
    - Создать суперпользователя Django:
    ```
    sudo docker-compose exec backend python manage.py createsuperuser
    ```
    - Импортровать в БД ингредиенты, чтобы пользователи могли ими пользоваться при создании рецептов:  
    ```
    sudo docker-compose exec backend python manage.py import_ingredients
    ```
    - Заполнить БД начальными данными (необязательно):  
    ```
    sudo docker-compose exec backend python manage.py loaddata dump.json
    ```
    - Проект будет доступен по IP вашего сервера.

## Автор
[Амосова Анастасия](https://github.com/aoamosova)