FROM envoyproxy/envoy-alpine-dev:latest

RUN apk update && apk add py3-pip bash curl

WORKDIR /

COPY main.py ./

COPY requirements.txt ./

COPY ./start_service.sh ./

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod u+x start_service.sh

ENTRYPOINT ["/bin/sh", "/start_service.sh"]