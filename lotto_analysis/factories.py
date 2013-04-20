#!/usr/bin/env python
"""
Retrieves lotto objects from either the json file on the Illinois lottery page
Or from the database
"""
from datetime import date
from lotto_analysis import models
import json
import os
import urllib2

class lotto_factory:

    lotto_url_base = "http://www.illinoislottery.com/lottery/data/history/winners/all/pastYear.json"

    # Initialize the factory

    def __init__(self,game):
        self._lotto_game = game
        self.data_dir = os.getcwd().split('/')
        return

    # Retrieve lotto

    def retrieve_lotto (self):
        results = ''
        lotto_results = []
        
        if (self._is_database_available()):
            results = self.retrieve_from_db()
        else:
            results = self.retrieve_from_web_recent()
            
            # Pull results only relevant to game type 
            for result in results:
                if (result['col2'] == self._lotto_game):
                    lotto_obj = models.lotto(result['col3'][0],result['col1'])
                    lotto_results.append(lotto_obj)

        # Pull results that are only releveant to the game type
        
        return lotto_results

    def retrieve_from_db(self):
        return False

    def retrieve_from_web_recent(self):

        lotto_url = self.lotto_url_base
        lotto_results = urllib2.Request(lotto_url)
        json_result = json.loads(urllib2.urlopen(lotto_results).read())

        return json_result

    # Functions that do checks

    def _is_database_available(self):
        # flesh out this function later
        return False
