#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.Persistence import Persistence


def handle(text):
    logger = logging.getLogger('GasstationsIntent')
    logger.info("... executing Gasstations intent")
    fuel_prices = Persistence.read("tankerkoenig")
    if "Diesel" in text:
        gastype = "diesel"
    elif "Benzin" in text:
        gastype = "benzin"
    cheapest = {gastype: 100.0}
    for station in fuel_prices['stations']:
        if station[gastype] <= cheapest[gastype]:
            cheapest = station
    response = "Der günstigste {0} kostet gerade: {1}€, bei der Tankstelle {2}.".format(
        gastype,
        format(cheapest["diesel"], '.2f').replace('.', ','),
        cheapest["name"]
    )
    return response

def is_requested(intent):
    return ("GasPrice" == intent)