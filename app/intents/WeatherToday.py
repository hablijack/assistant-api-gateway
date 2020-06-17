#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.Persistence import Persistence


def handle(text):
    logger = logging.getLogger('WeatherTodayModule')
    logger.info("... executing weather today module")
    forecast = Persistence.read("wetteronline")
    return forecast['today']

def is_requested(intent):
    return (intent == "WeatherToday")
