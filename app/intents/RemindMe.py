#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.Frontend import Frontend


def handle(text, slots, background_jobs):
    logger = logging.getLogger('ReminderModule')
    logger.info("... executing Reminder Module")
    if slots['hour'] and slots['minute']:
        hour = slots['hour']
        minute = slots['minute']
        identifier = 'timer' + str(hour) + str(minute)
        background_jobs.scheduler.add_job(
            id=identifier,
            func=execute_timer,
            args=[background_jobs, identifier, hour, minute],
            trigger='cron', 
            day_of_week='*',
            hour=hour, 
            minute=minute)
    return 'Verstanden! Ich werde Dich um: ' + str(hour) + ':' + str(minute) + ' Uhr erinnern.'

def execute_timer(background_jobs, identifier, hour, minute):
    logger = logging.getLogger('ActiveTimer')
    logger.info("... it is time for our reminder: EXECUTE IT")
    Frontend().say('Achtung! Es ist jetzt ' + str(hour) + ':' + str(minute) + ' Uhr! Hier deine Erinnerung.')
    background_jobs.scheduler.remove_job(identifier)
    logger.info("... reminder successfully executed : DELETE IT")

def is_requested(intent):
    return (intent == "RemindMe")