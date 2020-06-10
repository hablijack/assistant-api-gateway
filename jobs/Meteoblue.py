#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import logging


class Meteoblue:

    @staticmethod
    def fetch():
        logger = logging.getLogger('Meteoblue')
        logger.info("... requesting meteoblue weather data")
        page = requests.get('https://www.meteoblue.com/de/wetter/woche/waldershof_deutschland_2815048')
        soup = BeautifulSoup(page.text, 'html.parser')
        report_container = soup.find(class_='report')
        return report_container.find("p").text