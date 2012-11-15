#!/usr/bin/env python

from datetime import date
import json
import lib.models.lotto
import os
import urllib2

class lotto_factory:

    lotto_url_base = "http://www.illinoislottery.com/content/dam/ill/searchbyyear/";

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
        
        #FIXME maybe Im a python noob but it seems odd to me that I cannot
        # get if (self._is_database_available) to work on its own. I have to
        # specify is True. is that needed?

        if (self._is_database_available is True):
            results = self.retrieve_from_db()
        else:
            results = self.retrieve_from_web_recent()

        # Pull results that are only releveant to the game type
        #Massage results into json
        #json.load(results)
        return results 

    def retrieve_from_db(self):
        return False

    def retrieve_from_web_recent(self):
        today = date.today()
        year = today.year

        lotto_url = self.lotto_url_base+str(year)+".json"
        lotto_results = urllib2.Request(lotto_url)
        response = urllib2.urlopen(lotto_results)

        return response.read()

    # Functions that do checks

    def _is_database_available(self):
        # flesh out this function later
        return False
