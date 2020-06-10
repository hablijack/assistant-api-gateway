#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import feedparser
import logging
from library.Persistence import Persistence


class Tagesschau():

    @staticmethod
    def fetch():
        logger = logging.getLogger("Tagesschau")
        logger.info("fetching tagesschau 100s podcast")
        tagesschau_base_url = 'http://www.tagesschau.de'
        tagesschau_100s_url = '/export/podcast/hi/tagesschau-in-100-sekunden/'
        try:
            feed = feedparser.parse(tagesschau_base_url + tagesschau_100s_url)
            Persistence.persist('tagesschau', {'url': feed['entries'][0]['links'][0]['href']})
        except Exception as e:
            logger.error("Error: %s. Cannot get tagesschau." % e)
            Persistence.persist('tagesschau',  {})