#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import logging


class Wetteronline:

    @staticmethod
    def fetch():
        logger = logging.getLogger('Wetteronline')
        logger.info("... requesting wetteronline weather data")
        page = requests.get('https://www.wetteronline.de/wetter/waldershof')
        soup = BeautifulSoup(page.text, 'html.parser')
        report_container = soup.find_all(class_=['today'])
        today = report_container[1].text
        report_container = soup.find_all(class_=['tomorrow'])
        tomorrow = report_container[1].text
        return { 'today': today, 'tomorrow': tomorrow}
