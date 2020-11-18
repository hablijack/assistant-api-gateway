#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import datetime


def handle(text, scheduler):
    logger = logging.getLogger('TimeinfoModule')
    logger.info("... executing Timeinfo module")
    now = datetime.datetime.now()
    sentence = "Es ist jetzt " + str(now.hour) + "Uhr"
    if now.minute > 0:  
        sentence += " und " + str(now.minute) + "Minuten."
    return sentence

def is_requested(intent):
    return (intent == "GetTime")
