FROM python:3.10-alpine

COPY main.py /app/main.py
COPY ./requirements.txt /app/requirements.txt
# Print a phrase with the environment variable
RUN echo "The value of MY_VARIABLE_NAME is $CONFIG_FILE_PATH"
RUN pip install -r /app/requirements.txt

WORKDIR /app



ENTRYPOINT ["python", "/app/main.py"]