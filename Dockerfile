FROM python:3.8.8

WORKDIR /home/

RUN echo "testing22"

RUN git clone https://github.com/Adrian123K/AA.git

WORKDIR /home/AA/easyalert/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=easyalert.settings.deploy && python manage.py migrate --settings=easyalert.settings.deploy && gunicorn easyalert.wsgi --env DJANGO_SETTINGS_MODULE=easyalert.settings.deploy --bind 0.0.0.0:8000"]