#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, Response, send_from_directory, jsonify
from gevent.pywsgi import WSGIServer
from library.Configuration import Configuration
from library.Brain import Brain

app = Flask(__name__)


class Webserver():

    def __init__(self):
        self.http_server = WSGIServer(('', Configuration().app_port()), app, log=None)

    def serve(self):
        self.http_server.serve_forever()

    @staticmethod
    @app.route('/intent', methods=['POST'])
    def intent_handling():
        data = request.get_json()
        return Brain().execute_command_by_spoken_words(data['intent']['name'], data['text'])

    @staticmethod
    @app.route('/health')
    def health():
        return {'status': 'UP'}