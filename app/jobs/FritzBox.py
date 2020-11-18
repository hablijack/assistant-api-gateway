#!/usr/bin/python3
# -*- coding: utf-8 -*-

from fritzconnection.lib.fritzhosts import FritzHosts
import logging
from library.Configuration import Configuration
from library.Persistence import Persistence


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
            presence = []
            for index, host in enumerate(hosts, start=1):
                if host['name'] == "HandyBabs":
                    presence.append({'name': 'barbara', 'status': host['status']})
                elif host['name'] == "iPhoneChristoph":
                    presence.append({'name': 'christoph', 'status': host['status']})
            Persistence.persist('presence', presence)
        except Exception as e:
            logger.error("Error: %s. Cannot get fritzbox api." % e)
            Persistence.persist('presence',  {})