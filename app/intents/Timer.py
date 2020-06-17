#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import re


def handle(text):
    logger = logging.getLogger('TimerModule')
    logger.info("... executing Timer module")
    antwort = ""
    if 'Minuten' in text:
        result = re.findall(r'\d+', text)
        if len(result) > 0:
            if int(result[0]) == 1:
                answer = 'Eine Minute timer ab jetzt.')
            else:
                answer = str(result[0]) + ' Minuten timer ab jetzt.')
            try:
                subprocess.Popen(['python3', '../timer.py', str(result[0])])
            except:
                print("Fehler beim timer script")
        else:
            answer = 'Ich konnte keine Zeitangabe für deinem Timer ermitteln.')
    else:
        answer = 'Mit dieser Timer Angabe kann ich nichts anfangen.')
    return answer

def is_requested(intent):
    return (intent == "GetTimer")
