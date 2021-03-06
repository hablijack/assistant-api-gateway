#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.Frontend import Frontend


def handle(text, slots, background_jobs):
    logger = logging.getLogger('TimerModule')
    logger.info("... executing Timer Module")
    if slots['minutes']:
        minutes = slots['minutes']
        identifier = 'timer-time' + str(minutes)
        background_jobs.scheduler.add_job(
            id=identifier,
            func=execute_timer,
            args=[background_jobs, identifier, minutes],
            trigger='interval', 
            minutes=minutes)
    return 'Verstanden! Ich werde Dich in: ' + str(minutes) + ' Minuten erinnern.'

def execute_timer(background_jobs, identifier, minutes):
    logger = logging.getLogger('ActiveTimer')
    logger.info("... it is time for our reminder: EXECUTE IT")
    Frontend().say('Achtung! Deine ' + str(minutes) + ' Minuten Erinnerung ist soeben abgelaufen!')
    background_jobs.scheduler.remove_job(identifier)
    logger.info("... reminder successfully executed : DELETE IT")

def is_requested(intent):
    return (intent == "Timer")