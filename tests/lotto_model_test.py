#!/usr/bin/env python
"""
Unit Test for lotto model in models.py
"""
import sys
import unittest
import inspect

sys.path[0:0] = [""]
from lotto_analysis import models

class lotto_model_test(unittest.TestCase):

    def setUp(self):
        self.num_string = '01-02-03-04-05'
        self.draw_date = '04/15/2013'

    def test_create(self):
        lotto_obj = models.lotto(self.num_string,self.draw_date)
        self.assertEqual(lotto_obj.get_game(),'Lotto')

suite = unittest.TestLoader().loadTestsFromTestCase(lotto_model_test)
unittest.TextTestRunner(verbosity=2).run(suite)
