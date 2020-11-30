#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.Configuration import Configuration
from library.Persistence import Persistence
from library.Frontend import Frontend
from library.Fritzbox import Fritzbox


class Telephone:

    @staticmethod
    def fetch():
        logger = logging.getLogger('Telephone')
        logger.info("requesting fritzbox phonecall infos")
        try:
            config = Configuration()
            fbox = Fritzbox(
                config.fritzbox_ip(), 
                'phone', 
                config.fritzbox_password()
            ) 
            all_calls = fbox.get_call_history()
            Persistence.persist('calls', all_calls)
        except Exception as e:
            logger.error("Error: %s. Cannot get fritzbox api." % e)
            Persistence.persist('call_history', [])