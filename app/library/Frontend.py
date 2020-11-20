#!/usr/bin/python3
# -*- coding: utf-8 -*-

from library.Configuration import Configuration
import requests
import logging


class Frontend():
    def __init__(self):
        self.logger = logging.getLogger('Frontend')
        self.frontend_host = Configuration().frontend_host()

    def say(self, text):
        self.logger.info("... trying to say:" + text)
        url = self.frontend_host + '/api/text-to-speech'
        requests.post(url, data = text)
