#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.Persistence import Persistence
from datetime import datetime, timedelta


def handle(text, slots, scheduler):
    logger = logging.getLogger('WeatherModule')
    logger.info("... executing weather module")
    maschinenring = Persistence.read("maschinenring")
    answer = ''
    requested_day = {}
    day_text = ''
    if "heute" in text:
        day_text = 'heute'
        for day in maschinenring['weather']:
            if datetime.fromtimestamp(day['day']).date() == datetime.now().date():
                requested_day = day
                break
    elif "morgen" in text:
        day_text = 'morgen'
        for day in maschinenring['weather']:
            if datetime.fromtimestamp(day['day']).date() == datetime.now().date() + exitimedelta(days=1):
                requested_day = day
                break
    answer = ('Das Wetter in Waldershof wird ' 
        + day_text 
        + ' ' 
        + requested_day['condition'] 
        + ' bei Temperaturen zwischen ' 
        + str(requested_day['min_temp']) 
        + ' und '
        + str(requested_day['max_temp'])
        + ' Grad.'
        + ' Es wird ' 
        + day_text 
        + ' mit ' 
        + str(requested_day['prec_prob'])
        + ' Prozent Wahrscheinlichkeit ' 
        + str(requested_day['prec_amount'])
        + requested_day['prec_text']
        + ' geben.')
    return answer

def is_requested(intent):
    return (intent == "Weather")
