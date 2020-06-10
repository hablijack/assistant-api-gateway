#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import datetime
import json
import dateparser
from library.Configuration import Configuration
import logging


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
        req = requests.get(url, headers=headers)
        events = json.loads(req.text)
        agenda = []
        for event in events['events']:
            if event['subcalendar_id'] == 4377496:
                # Geburtstage
                event_date_string = dateparser.parse(event['start_dt']).strftime("%d.%m.%y")
            elif event['subcalendar_id'] == 4377396:
                # Feiertage
                event_date_string = dateparser.parse(event['start_dt']).strftime("%d.%m.%y")
            else:
                # Others
                event_date_string = dateparser.parse(event['start_dt']).strftime("%d.%m.%y %H:%M")
            e = event_date_string + " " + event['title']
            agenda.append(e)
        return agenda
