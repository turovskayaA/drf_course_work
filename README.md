# Docker (drf_course_work)

Для Docker-compose сформированы файлы с настройками docker-compose.yaml и Dockerfile. 

Для формирования контейнера с модулями приложения, Redis, БД Postresql, Celery и Celery-beat необходимо ввести команду docker-compose up -d --build (для миграций и доступов в файле учтены команды "python manage.py migrate && python manage.py runserver 0.0.0.0:8000") Для создания суперюзера необходимо ввести команду docker-compose exec app python manage.py csu
