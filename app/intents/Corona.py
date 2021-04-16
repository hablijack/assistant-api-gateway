#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.Persistence import Persistence


def handle(text, slots, scheduler):
    logger = logging.getLogger('CoronaIntent')
    logger.info("... executing Corona intent")
    incident = Persistence.read("corona")
    response = "Der aktuelle 7 Tage Inzidenzwert pro 100000 Einwohner im Landkreis Tirschenreuth beträgt: " + incident
    return response


def is_requested(intent):
    return ("Corona" == intent)
