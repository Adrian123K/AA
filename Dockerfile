FROM python:3.8.8

WORKDIR /home/

RUN git clone https://github.com/Adrian123K/AA.git

WORKDIR /home/AA/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-8u-%0v8+6oypi%+dymn@o0am^m&0e8nalh)k$4_%=5o&94+qb4" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]