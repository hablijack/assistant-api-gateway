#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json


class Persistence():

    @staticmethod
    def persist(id, data):
        filepath = '../cache/' + id + '.json'
        with open(filepath, 'w') as outfile:
            json.dump(data, outfile, sort_keys=True, indent=4)

    @staticmethod
    def read(id):
        filepath = '../cache/' + id + '.json'
        with open(filepath, 'r') as reader:
            json_str = reader.read()
            return json.loads(json_str)
