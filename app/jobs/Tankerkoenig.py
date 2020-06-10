#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json
from library.Configuration import Configuration
import logging
from library.Persistence import Persistence


class Tankerkoenig():

    @staticmethod
    def fetch():
        logger = logging.getLogger("Tankerkoenig")
        logger.info("... fetching tankerkoenig api")
        config = Configuration()
        lati = config.tankerkoenig_lat()
        longi = config.tankerkoenig_long()
        api_key = Configuration().tankerkoenig_api_key()

        tankerkoenig_url = 'https://creativecommons.tankerkoenig.de/json/list.php?lat=' + lati + '&lng=' + longi + '&rad=5&sort=dist&type=all&apikey='
        try:
            r = requests.get(tankerkoenig_url + api_key)
            json_obj = json.loads(r.content.decode('utf-8'))
            Persistence.persist('tankerkoenig', {'stations': json_obj['stations']})
        except Exception as e:
            logger.error("Error: %s. Cannot get tankerkoenig api." % e)
            Persistence.persist('tankerkoenig',  {})