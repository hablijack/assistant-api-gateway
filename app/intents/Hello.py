#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import logging


def handle(text):
    logger = logging.getLogger('HelloIntent')
    logger.info("... executing Hello intent")
    return random.choice(['Hallo! Wie kann ich helfen?', "Hallo!", "Hallo! Stets zu Diensten."])

def is_requested(intent):
    return ("Hallo" in intent)
