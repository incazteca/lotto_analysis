#!/usr/bin/env python

import json
import lib.models.lotto
import urllib2
import os

class lotto_factory:

    # Initialize the factory

    def __init__(self,game):
        self._lotto_game = game
        self.data_dir = os.getcwd().split('/')
        return

    def retrieve_lotto (self,game_type):
        if self._lotto_game is None:
            self._lotto_game = game_type

        results = self.retrieve_from_web()

        #Massage results into json
        json_results = results

        return json_results

    def retrieve_from_web(self):
        lotto_url = "http://www.illinoislottery.com/content/dam/ill/searchbyyear/2012.json"
        lotto_results = urllib2.Request(lotto_url)
        response = urllib2.urlopen(lotto_results)
        return response.read()
   
    # Functions that do checks

    def _is_database_available(self):
        # flesh out this function later
        return false
