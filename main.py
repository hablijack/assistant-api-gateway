#!/usr/bin/python3
# -*- coding: utf-8 -*-

from apscheduler.schedulers.background import BackgroundScheduler
import logging

from library.Scheduler import Scheduler
from library.Webserver import Webserver

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s [%(name)s] %(message)s",
        datefmt='%d.%m.%Y %H:%M:%S',
        handlers=[
            logging.StreamHandler()
        ]
    )

    scheduler = Scheduler()
    scheduler.start()

    webserver = Webserver()
    webserver.serve()