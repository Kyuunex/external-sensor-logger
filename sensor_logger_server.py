#!/usr/bin/env python3

import json
import time
from pathlib import Path, PosixPath
from flask import Flask, request, Response

app = Flask(__name__)

SAVE_PATH = PosixPath("~/.local/share/sensor_logger/").expanduser()
Path(SAVE_PATH).mkdir(parents=True, exist_ok=True)


@app.route('/sensor_logger', methods=['POST']) 
def sensor_logger():
    with open(f"{SAVE_PATH}/{request.remote_addr}-{time.time()}.json", "w") as outfile:
        json.dump(request.json, outfile)
    return Response('{"status":"success"}', status=201, mimetype='application/json')


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=3000,
        debug=True
    )
