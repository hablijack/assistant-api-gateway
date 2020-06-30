#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.Persistence import Persistence
import requests
import json


def handle(text):
    logger = logging.getLogger('NewsModule')
    logger.info("... executing News module")
    url = Persistence.read("tagesschau")
    requests.post("http://192.168.178.52:5000/change", json={"topic": "news", "url": url})
    return "Hier ist die aktuelle ARD Tagesschau."

def is_requested(intent):
    return ("Tagesschau" == intent)
