#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import pathlib
import os.path


class Persistence():

    @staticmethod
    def cache_exists(id):
        return os.path.isfile(str(pathlib.Path(__file__).parent.absolute()) +'/../cache/' + id + '.json') 

    @staticmethod
    def persist(id, data):
        filepath = str(pathlib.Path(__file__).parent.absolute()) +'/../cache/' + id + '.json'
        with open(filepath, 'w') as outfile:
            json.dump(data, outfile, sort_keys=True, indent=4)

    @staticmethod
    def read(id):
        filepath = str(pathlib.Path(__file__).parent.absolute()) + '/../cache/' + id + '.json'
        with open(filepath, 'r') as reader:
            json_str = reader.read()
            return json.loads(json_str)
