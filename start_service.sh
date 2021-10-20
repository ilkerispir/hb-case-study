#!/bin/sh
python3 main.py &
envoy -c /etc/service-envoy.yaml --service-cluster "service${SERVICE_NAME}"