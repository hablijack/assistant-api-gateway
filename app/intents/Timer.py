#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging


def handle(text, slots, scheduler):
    logger = logging.getLogger('TimerModule')
    logger.info("... executing Timer module")
    if slots['hour'] and slots['minute']:
        scheduler.add_job(
            id='timer',
            func=execute_timer,
            args=[scheduler],
            trigger='cron'
        )

def execute_timer(scheduler):
    logger = logging.getLogger('ActiveTimer')
    logger.info("... it is time for our timer: EXECUTE IT")
    scheduler.remove_job('timer')

def is_requested(intent):
    return (intent == "Timer")
