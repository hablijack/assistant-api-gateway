#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Call-Types
# 1-2 incoming?
#   3 out
#   10 blocked
#   11 call running at the moment

import html
import urllib.request
from lxml import etree
from typing import List
from fritzconnection import (FritzConnection)

class Fritzbox:

    def __init__(self, ip, user, password):
        self.connection = FritzConnection(address=ip, user=user, password=password)

    def get_call_history(self):
        # get the URL to the xml file with all calls
        calllisturl = self.connection.call_action('X_AVM-DE_OnTel', 'GetCallList')['NewCallListURL']
        # downlod xml file, parse it and get root node
        root = etree.parse(calllisturl).getroot()
        # list of all new/unprocessed incoming calls
        callerList = []
        for call in root.iter("Call"): # iterate through calls
            # new incoming call?
            if self.get_xml_child(call, 'Type') not in ["3", "11"]:
                callerNumber = self.get_xml_child(call, 'Caller') # get caller-number
                callDate = self.get_xml_child(call, 'Date') # get date
                callDuration = self.get_xml_child(call, 'Duration') # get duration
                callerName = self.get_xml_child(call, 'Name') # get name from addressbook
                callId = int(self.get_xml_child(call, 'Id'))
                newcall = {
                    'id' :  callId,
                    'number' : callerNumber, 
                    'date' : callDate, 
                    'duration' : callDuration, 
                    'name' : callerName
                }
                callerList.append(newcall)
        return callerList

    def get_xml_child(self, parent, attrname):
        """returns None if no child with that name or if the first is empty"""
        allattrs = parent.findall('.//'+attrname)
        if len(allattrs) > 0:
            return allattrs[0].text
        else:
            return None

    @staticmethod
    def telefonbuch_reverse_lookup(self, phonenumber):
        # now try to find that number with an reverse lookup
        try:
            dt_url = 'http://www.dastelefonbuch.de/R%C3%BCckw%C3%A4rts-Suche/'
            url = dt_url + phonenumber
            with urllib.request.urlopen(url) as response:
                START = '<div class="name" title="'
                STOP = '">'
                htmlContent = str(response.read().decode('utf-8'))
                posA = htmlContent.find(START) + len(START) # find start of name
                posB = htmlContent.find(STOP, posA) # find end of name
                # print("dast len: ",len(START),"posA: ",posA," posB",posB)
                if posA - len(START) < 0 or posB == -1:
                    raise Exception('Not found in dastelefonbuch')
                name = htmlContent[posA:posB] # get name
                name = name[:min(len(name), 10)]
                # we unescape html escape sequences like &ouml etc.
                return html.unescape(str(name))
        except:
            pass