FROM python:3.10

COPY . /app
WORKDIR /app

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]