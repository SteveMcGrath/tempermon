#!/usr/bin/env python
from bottle import Bottle, run, request, response, debug, static_file, template
from pymongo import MongoClient
from datetime import datetime
from ConfigParser import ConfigParser
import os
import json
import time
import bleach

app = Bottle()
conn = MongoClient()
db = conn.tempermon
devices = db.devices


@app.get('/static/<path:path>')
def statics(path):
    print path
    return static_file(path, root='static')


@app.post('/update')
def update_temp():
    name = bleach.clean(request.forms.name or None)
    temp = bleach.clean(request.forms.temp or None)
    tid = None
    if name is not None and temp is not None:
        device = devices.find_one({'name': name})
        if device is None:
            device = {'name': name}
        device['temp'] = temp
        device['time'] = int(time.time())
        devices.save(device)
    return temp_info(name)


@app.get('/')
def index():
    return template('homepage', devices=list(devices.find({})))


@app.get('/show/<name>')
def show_info(name):
    device = devices.find_one({'name': name})
    device['time'] = datetime.fromtimestamp(int(device['time'])).ctime()
    return template('device', device=device)


@app.get('/devices')
def device_list():
    response.set_header('Content-Type', 'application/json')
    response.set_header('Access-Control-Allow-Origin', '*')
    return json.dumps([i['name'] for i in devices.find({})])


@app.get('/devices/<name>')
def temp_info(name):
    response.set_header('Content-Type', 'application/json')
    response.set_header('Access-Control-Allow-Origin', '*')
    return json.dumps(devices.find_one({'name': name}, {'_id': 0}))


if __name__ == '__main__':
    os.chdir(os.path.join(os.path.dirname(__file__)))
    config = ConfigParser()
    config.read('svc.conf')
    debug(config.getboolean('Settings', 'debug'))
    run(app=app,
        port=config.getint('Settings', 'port'),
        host=config.get('Settings', 'address'),
        server=config.get('Settings', 'app_server'),
        reloader=config.getboolean('Settings', 'debug')
    )
