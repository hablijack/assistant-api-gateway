#!/usr/bin/python3
# -*- coding: utf-8 -*-

from apscheduler.schedulers.background import BackgroundScheduler

from jobs.ADAC import ADAC
from jobs.Chefkoch import Chefkoch
from jobs.Pollenflug import Pollenflug
from jobs.Posteo import Posteo
from jobs.Sueddeutsche import Sueddeutsche
from jobs.Tagesschau import Tagesschau
from jobs.Tankerkoenig import Tankerkoenig
from jobs.Teamup import Teamup
from jobs.Maschinenring import Maschinenring
from jobs.Telephone import Telephone
from jobs.CoronaIncident import CoronaIncident


class Scheduler():

    def __init__(self):
        ADAC.fetch()
        Chefkoch.fetch()
        Pollenflug.fetch()
        Posteo.fetch()
        Sueddeutsche.fetch()
        Tagesschau.fetch()
        Tankerkoenig.fetch()
        Teamup.fetch()
        Maschinenring.fetch()
        Telephone.fetch()
        CoronaIncident.fetch()
        self.scheduler = BackgroundScheduler()
        self.register_jobs()

    def start(self):
        self.scheduler.start()

    def register_jobs(self):
        self.scheduler.add_job(ADAC.fetch, 'interval', minutes=15)
        self.scheduler.add_job(Chefkoch.fetch, 'interval', days=1)
        self.scheduler.add_job(Telephone.fetch, 'interval', minutes=5)
        self.scheduler.add_job(Pollenflug.fetch, 'interval', minutes=30)
        self.scheduler.add_job(Posteo.fetch, 'interval', minutes=2)
        self.scheduler.add_job(Sueddeutsche.fetch, 'interval', minutes=20)
        self.scheduler.add_job(Tagesschau.fetch, 'interval', hours=4)
        self.scheduler.add_job(Tankerkoenig.fetch, 'interval', hours=1)
        self.scheduler.add_job(Teamup.fetch, 'interval', minutes=10)
        self.scheduler.add_job(Maschinenring.fetch, 'interval', hours=2)
        self.scheduler.add_job(CoronaIncident.fetch, 'interval', hours=1)
