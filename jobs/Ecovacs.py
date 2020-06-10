#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sucks import *
from library.Configuration import Configuration
import logging


class Ecovacs:

    areaTranslation = {
        "Wohnzimmer": "6",
        "Esszimmer": "0",
        "Bad": "2",
        "Diele": "1",
        "Garderobe": "4",
        "Eingang": "5",
        "Küche": "3"
    }

    def __init__(self, config):
        logger = logging.getLogger("Ecovacs")
        config = Configuration()
        self.ecovacs_password_hash = config.ecovacs_password_hash()
        self.ecovacs_email = config.ecovacs_email()  
        self.ecovacs_device_id = config.ecovacs_device_id()
        api = EcoVacsAPI(self.ecovacs_device_id, self.ecovacs_email, self.ecovacs_password_hash, "de", "eu")
        my_vac = api.devices()[0]
        self.vacbot = VacBot(api.uid, api.REALM, api.resource, api.user_access_token, my_vac, "eu")
        self.vacbot.connect_and_wait_until_ready()

    def common_cleanup(self):
        self.vacbot.run(SpotArea('start', area="0,1,2,3,4,5,6"))
        return "Berta, aufwachen! Fang an zu saugen!"

    def area_cleanup(self, slot):
        clean_area = ""
        for area in self.areaTranslation.keys():
            if area.lower() in slot.lower():
                clean_area = area
                break
        self.vacbot.run(SpotArea('start', area=clean_area))
        return "Berta, aufwachen! {0} saugen!".format(clean_area)

    def charging(self):
        self.vacbot.run(Charge())
        return "Berta, geh aufladen!"

    def stop_cleanup(self):
        self.vacbot.run(Stop())
        return "Berta, sofort aufhören!"