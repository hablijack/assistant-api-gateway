#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json
from library.Configuration import Configuration
import logging


class DarkSky:

    @staticmethod
    def fetch():
        logger = logging.getLogger("DarkSky")
        logger.info("fetching DarkSky Weather API")
        config = Configuration()
        token = config.darksky_token()
        latitude = config.darksky_waldershof_lat()
        longitude = config.darksky_waldershof_long()
        url = 'https://api.darksky.net/forecast/' + token + '/' + latitude + ',' + longitude + '?lang=de&exclude=minutely,flags,hourly&units=ca'
        return json.loads(requests.get(url).text)
