FROM alpine:3.10

COPY main.py /app/main.py
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

WORKDIR /app

CMD ["python", "/app/main.py"]