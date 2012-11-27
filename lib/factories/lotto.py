#!/usr/bin/env python

from datetime import date
import json
import lib.models.lotto
import os
import urllib2

class lotto_factory:

    #lotto_url_base = "http://www.illinoislottery.com/content/dam/ill/searchbyyear/";
    lotto_url_base = "http://www.illinoislottery.com/lottery/data/history/winners/all/pastYear.json"

    # Initialize the factory

    def __init__(self,game):
        self._lotto_game = game
        self.data_dir = os.getcwd().split('/')
        return

    # Retrieve lotto

    def retrieve_lotto (self,game_type):
        if self._lotto_game is None:
            self._lotto_game = game_type
        
        results = ''
        
        if (self._is_database_available()):
            results = self.retrieve_from_db()
        else:
            results = self.retrieve_from_web_recent()

        # Pull results that are only releveant to the game type
        
        lotto_result = []

        for result in results:
            if (result['col2'] == self._lotto_game):
                lotto_obj = lib.models.lotto.lotto(result['col3'],result['col1'])
                lotto_result.append(lotto_obj)


        return lotto_results

    def retrieve_from_db(self):
        return False

    def retrieve_from_web_recent(self):
        today = date.today()
        year = today.year

        lotto_url = self.lotto_url_base+str(year)+".json"
        lotto_results = urllib2.Request(lotto_url)
        json_result = json.loads(urllib2.urlopen(lotto_results).read())

        return json_result

    # Functions that do checks

    def _is_database_available(self):
        # flesh out this function later
        return False
