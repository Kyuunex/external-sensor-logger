#!/bin/bash
while :
do
    curl -d "$(sensors -j)" -H "Content-Type: application/json" -X POST "http://192.168.6.200:3000/sensor_logger"
    sleep 0.2
done
