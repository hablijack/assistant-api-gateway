#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.Persistence import Persistence


def handle(text):
    logger = logging.getLogger('NewsModule')
    logger.info("... executing News module")
    return Persistence.read("tagesschau")

def is_requested(intent):
    return ("Tagesschau" == intent)
