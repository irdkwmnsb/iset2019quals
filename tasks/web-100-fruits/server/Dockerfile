FROM python:3

WORKDIR /var/fruitfacts

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD gunicorn -c gunicorn.conf.py fruitfacts:app