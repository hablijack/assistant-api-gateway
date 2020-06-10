FROM python:3

ADD app /app

RUN mkdir /app/cache

RUN pip install -r /app/requirements.txt

CMD [ "python", "/app/main.py" ]

EXPOSE 8080/tcp