#!/usr/bin/env python
"""
Unit Test for lotto factory in factories.py
"""
import sys
import unittest

sys.path[0:0] = [""]
from lotto_analysis import factories

class lotto_factory_test(unittest.TestCase):

    def setUp(self):
        self.num_string = '01-02-03-04-05'
        self.draw_date = '04/15/2013'

    def retrieve_lotto_game(self):
        lotto_obj = models.lotto(self.num_string,self.draw_date)

        # Ensure that object is a lotto object
        self.assertEqual(lotto_obj.get_game(),'Lotto')

suite = unittest.TestLoader().loadTestsFromTestCase(lotto_factory_test)
unittest.TextTestRunner(verbosity=2).run(suite)
