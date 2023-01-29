#!/usr/bin/env python3

import json
import time
import gzip
from pathlib import Path, PosixPath
from flask import Flask, request, Response

app = Flask(__name__)

logs = []


@app.route('/sensor_logger', methods=['POST']) 
def sensor_logger():
    request.json["timestamp"] = time.time()
    request.json["ip_address"] = request.remote_addr
    logs.append(request.json)

    response_dict = {
        "status": "success"
    }

    return Response(json.dumps(response_dict), status=201, mimetype='application/json')


@app.route('/export_to_internal_storage')
def export_to_internal_storage():
    save_path = PosixPath("~/.local/share/sensor_logger/").expanduser()
    Path(save_path).mkdir(parents=True, exist_ok=True)

    file_location = f"{save_path}/{time.time()}.json.gz"

    generated_json = json.dumps(logs)

    with gzip.open(file_location, "w") as outfile:
        outfile.write(bytes(generated_json, 'ascii'))
    del logs[:]

    response_dict = {
        "status": "success",
        "file_location": file_location
    }

    return Response(json.dumps(response_dict), status=201, mimetype='application/json')


@app.route('/export.json')
def export_json():
    generated_json = json.dumps(logs)
    del logs[:]
    return Response(generated_json, status=200, mimetype='application/json')


@app.route('/export.json.gz')
def export_json_gzip():
    generated_json = json.dumps(logs)
    del logs[:]
    gzip_bytes = gzip.compress(bytes(generated_json, 'ascii'))
    return Response(gzip_bytes, status=200, mimetype='application/x-gzip')


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=3000,
        debug=True
    )
