FROM python:3.7

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY app.py /app/app.py
COPY watershed.py /app/watershed.py

CMD [ "python" , "app.py"]

