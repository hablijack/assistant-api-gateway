#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import datetime
import json
import dateparser
from library.Configuration import Configuration
import logging
from library.Persistence import Persistence


class Teamup:

    @staticmethod
    def fetch():
        logger = logging.getLogger("Teamup")
        logger.info("... fetching Teamup API")
        config = Configuration()
        teamup_url = config.teamup_url()
        teamup_token = config.teamup_token()

        start_date = str(datetime.date.today())
        end_date = str(datetime.date.today() + datetime.timedelta(days=2))
        url = teamup_url + "/events" + "?startDate=" + start_date + "&endDate=" + end_date
        headers = {'Teamup-Token': teamup_token}
        try:
            req = requests.get(url, headers=headers)
            events = json.loads(req.text)
            Persistence.persist('teamup', events)
        except Exception as e:
            logger.error("Error: %s. Cannot get teamup calendar." % e)
            Persistence.persist('teamup',  {})