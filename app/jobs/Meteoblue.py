#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import logging
from library.Persistence import Persistence


class Meteoblue:

    @staticmethod
    def fetch():
        logger = logging.getLogger('Meteoblue')
        logger.info("requesting meteoblue weather data")
        try:
            page = requests.get('https://www.meteoblue.com/de/wetter/woche/waldershof_deutschland_2815048')
            soup = BeautifulSoup(page.text, 'html.parser')
            report_container = soup.find(class_='report')
            Persistence.persist('meteoblue', {'forecast': report_container.find("p").text})
        except Exception as e:
            logger.error("Error: %s. Cannot get meteoblue api." % e)
            Persistence.persist('meteoblue',  {})