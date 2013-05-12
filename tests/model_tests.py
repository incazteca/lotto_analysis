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

    def test_get_numbers(self):
        lotto_obj = models.lotto(self.num_string,self.draw_date)
        self.assertEqual(lotto_obj.get_numbers(),['01','02','03','04','05'])

    def test_get_draw_date(self):
        lotto_obj = models.lotto(self.num_string,self.draw_date)

        # Ensure that draw_date is a date object
        self.assertEqual(lotto_obj.get_draw_date().year,2013)
        self.assertEqual(lotto_obj.get_draw_date().month,4)
        self.assertEqual(lotto_obj.get_draw_date().day,15)

suite = unittest.TestLoader().loadTestsFromTestCase(lotto_model_test)
unittest.TextTestRunner(verbosity=2).run(suite)
