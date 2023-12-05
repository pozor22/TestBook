# TestBook 
Тестовое задание. 
Веб-приложение с API эндпоитами с возможностью создания, чтения, обновления информации и удаления книг.
Так же с возможностью создания пользователей и отправкой приветсвенного письма с использованием Celery

Стек технологий: Django, DRF, Celery, Docker, Mysql.

___
Для запуска контейнера необходимо перейти в корневую папку и запустить следующие команды:
```
docker-compose build
```
```
docker-compose up
```
Дальше необходимо провети миграции для базы данных для этого нужно использовать следующие команды:
```
docker compose run —rm web sh -c "python manage.py makemigrations"
```
```
docker compose run —rm web sh -c "python manage.py migrate"
```
И последняя команда необходима для создания супер админа для нашего приложения:
```
docker compose run —rm web sh -c "python manage.py createsuperuser"
```
И заполняем как сами)
