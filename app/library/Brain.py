#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pkgutil
import os
import logging

""""
Takes evaluated sentence from STT-Engine and tries to find fitting
command and let domino do the magic.
"""


class Brain:

    def __init__(self, scheduler):
        self.scheduler = scheduler
        self.logger = logging.getLogger('Brain')
        self.app_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
        locations = [os.path.join(self.app_path, "intents")]
        self.modules = []
        for finder, name, ispkg in pkgutil.walk_packages(locations):
            loader = finder.find_module(name)
            mod = loader.load_module(name)
            self.modules.append(mod)
        self.modules.sort(key=lambda mod: mod.PRIORITY if hasattr(mod, 'PRIORITY') else 0, reverse=False)

    def execute_command_by_spoken_words(self, intent, text):
        answer = ""
        for module in self.modules:
            if module.is_requested(intent):
                self.logger.info("... intent found for: " + intent)
                try:
                    self.logger.info("... executing module")
                    answer = module.handle(text, self.scheduler)
                except Exception as e:
                    self.logger.error("Error: %s on handling module!" % e)
                break
        if answer:
            return { "speech": { "text": answer } }
        else:
            return
