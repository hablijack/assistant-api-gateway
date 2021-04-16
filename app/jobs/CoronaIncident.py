#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import requests
from library.Persistence import Persistence


class CoronaIncident():

    @staticmethod
    def fetch():
        try:
            logger = logging.getLogger("Corona")
            logger.info("parsing corona card inzidenz recipe of the day")
            REQUST_URL = "https://www.lgl.bayern.de/gesundheit/infektionsschutz/infektionskrankheiten_a_z/coronavirus/karte_coronavirus/csv.htm?tabelle=tabelle4"
            headers = {'User-Agent': 'Mozilla/5.0'}
            page = requests.get(REQUST_URL, headers=headers)
            csvFile = page.content.decode('utf-8')
            incidenz = 0
            for line in iter(csvFile.splitlines()):
                if "Tirschenreuth" in line:
                    incidenz = line.split(';')[5]
                    break
            Persistence.persist('corona', {'inzidenz': incidenz})
        except Exception as e:
            logger.error('Error: %s. Cannot get corona api.' % e)
            Persistence.persist('corona',  {})
