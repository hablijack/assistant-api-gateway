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
    @app.route('/traffic')
    def adac():
        return Persistence.read('adac')
    
    @staticmethod
    @app.route('/recipe')
    def chefkoch():
        return Persistence.read('chefkoch')

    @staticmethod
    @app.route('/vaccuum/cleanup')
    def ecovacs():
        return {}

    @staticmethod
    @app.route('/weather')
    def weather():
        return Persistence.read('wetteronline')

    @staticmethod
    @app.route('/mails')
    def posteo():
        return Persistence.read('posteo')

    @staticmethod
    @app.route('/news')
    def sueddeutsche():
        return Persistence.read('sueddeutsche')

    @staticmethod
    @app.route('/newspodcast')
    def tagesschau():
        return Persistence.read('tagesschau')

    @staticmethod
    @app.route('/gasprice')
    def tankerkoenig():
        return Persistence.read('tankerkoenig')

    @staticmethod
    @app.route('/calendar')
    def teamup():
        return Persistence.read('teamup')

    @staticmethod
    @app.route('/health')
    def health():
        return {'status': 'UP'}