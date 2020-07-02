#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.Persistence import Persistence
import datetime
import dateparser

def handle(text):
    logger = logging.getLogger("CalendarIntent")
    logger.info("... executing Calendar intent")
    calendar = Persistence.read("teamup")
    agenda = ""
    for event in calendar['events']:
        user_names = []
        trashinfo = False
        TEAMUP_USERS = [
            {"name": "Christoph", "calendar_id": 4377398},
            {"name": "Barbara", "calendar_id": 4377397},
            {"name": "Family", "calendar_id": 4377538},
            {"name": "Feiertage", "calendar_id": 4377396},
            {"name": "Geburtstage", "calendar_id": 4377496},
            {"name": "Müll", "calendar_id": 7539853}
        ]
        for calendar_id in event["subcalendar_ids"]:
            for user in TEAMUP_USERS:
                if calendar_id == user["calendar_id"]:
                    user_names.append(user["name"])
                    break
        parsed_date = dateparser.parse(event["start_dt"]).date()
        if parsed_date == datetime.datetime.today().date():
            date_str = "heute "
        elif parsed_date == (datetime.datetime.date.today() + datetime.datetime.timedelta(days=1)).date():
            date_str = "morgen "
        else:
            date_str = "übermorgen "

        if user_names[0] == "Family":
            user_names[0] = "Barbara"
            user_names.append("Christoph")
        user_string = " und ".join(user_names)
        if len(user_names) > 1:
            user_string += " haben "
        else:
            user_string += " hat "
            if user_names[0] == "Müll":
                trashinfo = True

        user_string += date_str
        if trashinfo:
            agenda += "Achtung, " + date_str + " ist: " + event["title"] + "! "
        else:
            if event["all_day"]:
                agenda += user_string + "den ganzen Tag " + event["title"] + ". "
            else:
                time_string = event["start_dt"]
                event_time = datetime.datetime.strptime(time_string[:len(time_string)-3] + time_string[len(time_string)-2:], '%Y-%m-%dT%H:%M:%S%z')
                agenda += user_string + "um " + "{0:%H:%M}".format(event_time) + "Uhr " + event['title'] + ". "
        
    if len(calendar['events']) == 0:
        agenda = "Du hast heute und morgen keine Termine mehr."
    return agenda

def is_requested(intent):
    return ("Calendar" == intent)
