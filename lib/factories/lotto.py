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

        results = self.retrieve_from_web_recent()
        # Pull results that are only releveant to the game type
        #Massage results into json
        #json.load(results)
        return results 

    def retrieve_from_web_recent(self):
        today = date.today()
        lotto_url = lotto_url_base+year+".json"
        lotto_results = urllib2.Request(lotto_url)
        response = urllib2.urlopen(lotto_results)
        return response.read()

    def retrieve_from_web_year(self,year):
        lotto_url = lotto_url_base+year+".json"
        return response.read()
   
    # Functions that do checks

    def _is_database_available(self):
        # flesh out this function later
        return false
