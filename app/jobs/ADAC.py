#!/usr/bin/python3
# -*- coding: utf-8 -*-

import feedparser
from bs4 import BeautifulSoup
from library.Configuration import Configuration
import logging


class ADAC:

    @staticmethod
    def fetch():
        logger = logging.getLogger("ADAC")
        logger.info("requesting ADAC-API")
        adac_token = Configuration().adac_token()
        adac_50km_radius_rss_url = 'http://routenplaner.adac.de/util/RSSFeed.aspx?type=VerkehrsInfo&param=' + adac_token
        feed = feedparser.parse(adac_50km_radius_rss_url)
        incidents = feed['items']
        traffic_messages = []
        for incident in incidents:
            title = BeautifulSoup(incident['title'], 'html.parser')
            summary = BeautifulSoup(incident['summary'], 'html.parser')
            traffic_messages.append({'title': str(title), 'summary': str(summary)})
        return traffic_messages
