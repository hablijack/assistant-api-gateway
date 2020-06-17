#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, Response, send_from_directory, jsonify
from gevent.pywsgi import WSGIServer
from library.Configuration import Configuration
from library.Persistence import Persistence

app = Flask(__name__)


class Webserver():

    def __init__(self):
        self.http_server = WSGIServer(('', Configuration().app_port()), app, log=None)

    def serve(self):
        self.http_server.serve_forever()

    @staticmethod
    @app.route('/intent')
    def intent_handling():
        return { "speech": { "text": "Die Sprachausgabe funktioniert!"}}

    @staticmethod
    @app.route('/health')
    def health():
        return {'status': 'UP'}