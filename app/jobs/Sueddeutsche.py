#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import feedparser
import traceback
import logging


class Sueddeutsche():

    @staticmethod
    def fetch():
        logger = logging.getLogger("Sueddeutsche")
        logger.info("fetching sueddeutsche RSS Feeds")
        headline_url = "http://rss.sueddeutsche.de/rss/Topthemen"
        try:
            logger.info("getting feed")
            feed = feedparser.parse(headline_url)
            return feed.entries[0:5]
        except Exception as e:
            logger.error("Error: %s. Cannot get news." % e)
            return {}
