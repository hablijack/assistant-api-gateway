#!/usr/bin/python3
# -*- coding: utf-8 -*-

import imaplib
from library.Configuration import Configuration
import logging
from library.Persistence import Persistence


class Posteo():

    @staticmethod
    def fetch():
        logger = logging.getLogger("Posteo")
        logger.info("fetching posteo mails via imap")
        config = Configuration()
        mailhost = 'posteo.de'
        mailport = 993
        username = config.posteo_username()
        password = config.posteo_password()

        obj = imaplib.IMAP4_SSL(mailhost, mailport)
        obj.login(username, password)
        obj.select()
        count = len(obj.search(None, 'UnSeen')[1][0].split())
        Persistence.persist('posteo', {'count': count})
