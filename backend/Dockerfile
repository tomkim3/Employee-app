FROM tiangolo/uwsgi-nginx:python3.8

COPY . /application
WORKDIR /appapplication

ENV UWSGI_INI /application/uwsgi.ini
ENV PYTHONPATH=/application

RUN pip install -r /application/requirements.txt