#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.Persistence import Persistence


def handle(text):
    logger = logging.getLogger('WeatherTomorrowModule')
    logger.info("... executing weather tomorrow module")
    forecast = Persistence.read("wetteronline")
    return forecast['tomorrow']

def is_requested(intent):
    return "WeatherTomorrow" == intent
