#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging


def handle(text, slots, scheduler):
    logger = logging.getLogger('TimerModule')
    logger.info("... executing Timer module")
    logger.info(slots)

def is_requested(intent):
    return (intent == "Timer")
