#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sucks import *
from library.Configuration import Configuration
import logging


def handle(text, slots, scheduler):
    logger = logging.getLogger('VacuumRobotIntent')
    logger.info("... executing vacuum robot intent")
    config = Configuration()
    ecovacs_password_hash = config.ecovacs_password_hash()
    ecovacs_email = config.ecovacs_email()  
    ecovacs_device_id = config.ecovacs_device_id()
    api = EcoVacsAPI(ecovacs_device_id, ecovacs_email, ecovacs_password_hash, "de", "eu")
    my_vac = api.devices()[0]
    vacbot = VacBot(api.uid, api.REALM, api.resource, api.user_access_token, my_vac, "eu")
    vacbot.connect_and_wait_until_ready()

    answer = ""
    if "saugen" in text or "staubsaugen" in text:
        if "Wohnzimmer" in text:
            vacbot.run(SpotArea('start', area="5"))
            answer = "Berta, aufwachen! Sauge im Wohnzimmer!"
        elif "Esszimmer" in text:
            vacbot.run(SpotArea('start', area="0"))
            answer = "Berta, aufwachen! Sauge im Esszimmer!"
        elif "Bad" in text:
            vacbot.run(SpotArea('start', area="3"))
            answer = "Berta, aufwachen! Sauge im Bad!"
        elif "Diele" in text:
            vacbot.run(SpotArea('start', area="1"))
            answer = "Berta, aufwachen! Sauge in der Diele!"
        elif "Garderobe" in text:
            vacbot.run(SpotArea('start', area="4"))
            answer = "Berta, aufwachen! Sauge in der Garderobe!"
        elif "Eingang" in text:
            vacbot.run(SpotArea('start', area="6"))
            answer = "Berta, aufwachen! Sauge im Eingangsbereich!"
        elif "Küche" in text:
            vacbot.run(SpotArea('start', area="2"))
            answer = "Berta, aufwachen! Sauge in der Küche!"
        else:
            vacbot.run(SpotArea('start', area="0,1,2,3,4,5,6"))
            answer = "Berta, aufwachen! Fang an zu saugen!"
    elif "aufladen" in text or "Ladestation" in text:
        vacbot.run(Charge())
        answer = "Berta, geh aufladen!"
    elif "aufhören" in text or "anhalten" in text:
        vacbot.run(Stop())
        answer = "Berta, sofort aufhören!"
    return answer


def is_requested(intent):
    return intent == "Vacuum"
