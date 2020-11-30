#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.Configuration import Configuration
from library.Persistence import Persistence
from library.Frontend import Frontend
from library.Fritzbox import Fritzbox
from operator import itemgetter


class Telephone:

    @staticmethod
    def fetch():
        logger = logging.getLogger('Telephone')
        logger.info("requesting fritzbox phonecall infos")
        last_known_id = 0
        try:
            if Persistence.cache_exists('calls'):
                old_calls = Persistence.read('calls')
                if len(old_calls) > 0:
                    last_known_id = sorted(old_calls, key=itemgetter('id'), reverse=True)[0]['id']

            config = Configuration()
            fbox = Fritzbox(
                config.fritzbox_ip(), 
                'phone', 
                config.fritzbox_password()
            )
            
            if Persistence.cache_exists('missed_calls'):
                missed_calls = Persistence.read('missed_calls')
            else:
                missed_calls = []
            
            new_calls = fbox.get_call_history()
            for new_call in new_calls:
                if last_known_id != 0 and new_call['id'] > last_known_id and new_call['duration'] == "0:00":
                    if new_call['name'] == None:
                        new_call['name'] = Fritzbox.telefonbuch_reverse_lookup(new_call['number'])
                    missed_calls.append(new_call)

            Persistence.persist('calls', new_calls)
            Persistence.persist('missed_calls', missed_calls)
        except Exception as e:
            logger.error("Error: %s. Cannot get fritzbox api." % e)
            Persistence.persist('calls', [])