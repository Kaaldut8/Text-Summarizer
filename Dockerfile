FROM python:3.12-slim

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPR . /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]