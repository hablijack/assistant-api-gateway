#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import logging
from library.Persistence import Persistence


class Wetteronline:

    @staticmethod
    def fetch():
        logger = logging.getLogger('Wetteronline')
        logger.info("... requesting wetteronline weather data")
        try:
            page = requests.get('https://www.wetteronline.de/wetter/waldershof')
            soup = BeautifulSoup(page.text, 'html.parser')
            report_container = soup.find_all(class_=['today'])
            today = report_container[1].text
            report_container = soup.find_all(class_=['tomorrow'])
            tomorrow = report_container[1].text
            Persistence.persist('wetteronline',  { 'today': today, 'tomorrow': tomorrow})
        except Exception as e:
            logger.error("Error: %s. Cannot get Wetteronline api." % e)
            Persistence.persist('wetteronline',  {})