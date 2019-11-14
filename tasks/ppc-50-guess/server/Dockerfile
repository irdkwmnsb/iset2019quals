FROM python:3

WORKDIR /opt/ppc-50-guess

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY . .

CMD ["python3", "src/serve.py"]
