#!/usr/bin/python3
# -*- coding: utf-8 -*-

from apscheduler.schedulers.background import BackgroundScheduler
import logging
from library.Scheduler import Scheduler
from library.Configuration import Configuration
from waitress import serve
from flask import Flask, request
from library.Brain import Brain

app = Flask(__name__)
scheduler = Scheduler()

@app.route('/intent', methods=['POST'])
def intent_handling():
    data = request.get_json()
    return Brain(scheduler).execute_command_by_spoken_words(data)

@app.route('/health')
def health():
    return {'status': 'UP'}

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s [%(name)s] %(message)s",
        datefmt='%d.%m.%Y %H:%M:%S',
        handlers=[
            logging.StreamHandler()
        ]
    )
    scheduler.start()
    serve(app, port=Configuration().app_port())