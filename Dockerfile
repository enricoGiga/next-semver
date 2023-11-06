FROM alpine:3.10
COPY entrypoint.sh /app/entrypoint.sh
WORKDIR /app
# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/app/entrypoint.sh"]