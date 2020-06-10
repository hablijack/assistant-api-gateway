#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.Persistence import Persistence


class Pollenflug():

    @staticmethod
    def fetch():
        logger = logging.getLogger("Pollenflug")
        logger.info('fetching dwd pollenflug api')
        # https://maps.dwd.de/geoserver/dwd/wms?service=WMS&version=1.3&request=GetFeatureInfo&layers=Pollenflug_Graeser&styles=&bbox=5.866,47.27,15.042,55.057&width=512&height=434&srs=EPSG:4326&query_layers=Pollenflug_Graeser&x=283&y=346&info_format=application/json&FEATURE_COUNT=24&time=
