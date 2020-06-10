#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json
from library.Configuration import Configuration
import logging
from library.Persistence import Persistence


class DarkSky:

    @staticmethod
    def fetch():
        logger = logging.getLogger("DarkSky")
        logger.info("fetching DarkSky Weather API")
        config = Configuration()
        token = config.darksky_token()
        latitude = config.darksky_waldershof_lat()
        longitude = config.darksky_waldershof_long()
        try:
            url = 'https://api.darksky.net/forecast/' + token + '/' + latitude + ',' + longitude + '?lang=de&exclude=minutely,flags,hourly&units=ca'
            Persistence.persist('darksky', json.loads(requests.get(url).text))  
        except Exception as e:
            logger.error("Error: %s. Cannot get darksky api." % e)
