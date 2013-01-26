#!/usr/bin/env python
import temper
import os
import json
import sys
from urllib2 import urlopen, Request
from urllib import urlencode
from ConfigParser import ConfigParser

def update(config):
    '''Updates the JSON Service'''

    # First thing we need to do is instantiate the handler and get the first
    # device we see.  As I don't have multiple devices to test with, I will
    # only poll the first device I see.
    handler = temper.TemperHandler()
    devs = handler.get_devices()
    if len(devs) < 0:
        raise Exception('Could not Find any Devices')
    device = devs[0]

    # Next we need to get the temperature from the device and generate the
    # URL-Encoded Payload
    payload = urlencode({
        'name': config.get('Settings', 'name'),
        'temp': device.get_temperature(config.get('Settings', 'unit'))
    })

    # And lastly to send the update.
    urlopen(Request(config.get('Settings', 'url'), payload)).read()


if __name__ == '__main__':
    cfile = os.path.join(os.path.dirname(__file__), 'client.conf')
    config = ConfigParser()
    config.read(cfile)
    update(config)