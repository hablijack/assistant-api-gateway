#!/usr/bin/python3
# -*- coding: utf-8 -*-

from fritzconnection.lib.fritzhosts import FritzHosts
import logging
from library.Configuration import Configuration
from library.Persistence import Persistence
from library.Frontend import Frontend


class FritzBox:

    @staticmethod
    def fetch():
        logger = logging.getLogger('FritzBox')
        logger.info("requesting fritzbox host/wifi presence infos")
        try:
            config = Configuration()
            ip = config.fritzbox_ip()
            password = config.fritzbox_password()
            fh = FritzHosts(address=ip, password=password)
            hosts = fh.get_hosts_info()
            current_presence = {}
            for index, host in enumerate(hosts, start=1):
                if host['name'] == "HandyBabs":
                    current_presence['barbara'] = host['status']
                elif host['name'] == "iPhoneChristoph":
                    current_presence['christoph'] = host['status']
            
            # FANCY STUFF - TELL FRONTEND WHEN STATE CHANGES
            sentence = ''
            try:
                old_presence = Persistence.read('presence')
            except Exception as e:
                # First time run so we have no presence - take default one
                old_presence = {'barbara': False, 'christoph': False}

            if old_presence['barbara'] != current_presence['barbara']:
                sentence += 'Barbara '
                if current_presence['barbara'] == True:
                    sentence += 'kommt gerade nach Hause!'
                else:
                    sentence += 'geht gerade aus dem Haus!'
            elif old_presence['christoph'] != current_presence['christoph']:
                sentence += 'Christoph '
                if current_presence['christoph'] == True:
                    sentence += 'kommt gerade nach Hause!'
                else:
                    sentence += 'geht gerade aus dem Haus!'
            if len(sentence) > 1:
                Frontend().say(sentence)
            # FANCY STUFF ENDED

            Persistence.persist('presence', current_presence)
        except Exception as e:
            logger.error("Error: %s. Cannot get fritzbox api." % e)
            Persistence.persist('presence',  {'barbara': False, 'christoph': False})