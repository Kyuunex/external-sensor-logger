#!/bin/bash

IP_AND_PORT=$@

if ! command -v sensors &> /dev/null
then
    echo "lm-sensors is not installed!"
    exit
fi

if ! command -v curl &> /dev/null
then
    echo "curl is not installed!"
    exit
fi

while :
do
    curl -d "$(sensors -j)" -H "Content-Type: application/json" -X POST "http://$IP_AND_PORT/sensor_logger"
    sleep 0.2
done
