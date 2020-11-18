#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.Persistence import Persistence
import requests
import json


def handle(text, slots, scheduler):
    logger = logging.getLogger('NewsModule')
    logger.info("... executing News module")
    tagesschau = Persistence.read("tagesschau")
    requests.post("http://192.168.178.52:5000/change", json={"topic": "news", "url": tagesschau['url']})
    return None

def is_requested(intent):
    return ("Tagesschau" == intent)
