#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import logging
import json
from library.Persistence import Persistence


class Maschinenring:

    @staticmethod
    def fetch():
        logger = logging.getLogger('Maschinenring')
        logger.info("requesting maschinenring weather data")
        try:
            page = requests.get('https://www.maschinenring.de/?eID=weatherbaseWeatherHandler&action=api2_weather_7day_latlong&lat=49.9829487&long=12.0663612&elevation=')
            json_obj = json.loads(page.content.decode('utf-8'))
            Persistence.persist('maschinenring', {'weather': json_obj})
        except Exception as e:
            logger.error("Error: %s. Cannot get maschinenring api." % e)
            Persistence.persist('maschinenring',  {})
