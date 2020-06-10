#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

""""
Read configuration from environment variables
"""


class Configuration:

    def app_port(self):
        return int(os.getenv('APP_PORT'))

    def ecovacs_password_hash(self):
        return os.getenv('ECOVACS_PASSWORD_HASH')

    def ecovacs_email(self):
        return os.getenv('ECOVACS_EMAIL')

    def ecovacs_device_id(self):
        return os.getenv('ECOVACS_DEVICE_ID')

    def adac_token(self):
        return os.getenv('ADAC_TOKEN')

    def tankerkoenig_api_key(self):
        return os.getenv('TANKERKOENIG_API_KEY')

    def tankerkoenig_lat(self):
        return os.getenv('TANKERKOENIG_LAT')

    def tankerkoenig_long(self):
        return os.getenv('TANKERKOENIG_LONG')

    def posteo_username(self):
        return os.getenv('POSTEO_USERNAME')

    def posteo_password(self):
        return os.getenv('POSTEO_PASSWORD') 

    def teamup_token(self):
        return os.getenv('TEAMUP_TOKEN')

    def teamup_url(self):
        return os.getenv('TEAMUP_URL')

    def darksky_token(self):
        return os.getenv('DARKSKY_TOKEN')

    def darksky_waldershof_lat(self):
        return os.getenv('DARKSKY_LAT')

    def darksky_waldershof_long(self):
        return os.getenv('DARKSKY_LONG') 
