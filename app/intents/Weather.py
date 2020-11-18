#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.Persistence import Persistence


def handle(text, slots, scheduler):
    logger = logging.getLogger('WeatherModule')
    logger.info("... executing weather module")
    forecast = Persistence.read("wetteronline")
    answer = ""
    if "heute" in text:
        answer = forecast['today']
    elif "morgen" in text:
        answer = forecast['tomorrow']
    return answer

def is_requested(intent):
    return (intent == "Weather")
