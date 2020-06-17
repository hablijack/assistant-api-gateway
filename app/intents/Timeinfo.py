#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import datetime


def handle(text):
    logger = logging.getLogger('TimeinfoModule')
    logger.info("... executing Timeinfo module")
    now = datetime.datetime.now()
    return "Es ist jetzt " + str(now.hour) + "Uhr und " + str(now.minute) + "Minuten."

def is_requested(intent):
    return (intent == "GetTime")
