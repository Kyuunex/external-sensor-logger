#!/bin/sh

if [ -z "$1" ]
then
    echo "please specify IP:PORT as an argument!"
    exit
fi

if [ -z "$2" ]
then
    SLEEP_TIME=0.2
else
    SLEEP_TIME=$2
fi

IP_AND_PORT=$1
echo "sending sensor data every $SLEEP_TIME seconds"

if ! command -v sensors > /dev/null
then
    echo "lm-sensors is not installed!"
    exit
fi

if ! command -v curl > /dev/null
then
    echo "curl is not installed!"
    exit
fi

while :
do
    curl -d "$(sensors -j)" -H "Content-Type: application/json" -X POST "http://$IP_AND_PORT/sensor_logger"
    sleep "$SLEEP_TIME"
done
