FROM python:3.10-alpine

COPY main.py /app/main.py
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

WORKDIR /app



ENTRYPOINT ["python", "/app/main.py"]