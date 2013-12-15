#!/usr/bin/env python
"""
Unit Test for lotto model in models.py
"""
import sys
import unittest
import inspect

sys.path[0:0] = [""]
from lotto_analysis import models

class base_lotto_model_test(object):

    def test_get_draw_date(self):
        lotto_obj = models.lotto(self.num_string,self.draw_date)

        # Ensure that draw_date is a date object
        self.assertEqual(lotto_obj.get_draw_date().year,2013)
        self.assertEqual(lotto_obj.get_draw_date().month,4)
        self.assertEqual(lotto_obj.get_draw_date().day,15)

class lotto_model_test(unittest.TestCase, base_lotto_model_test):
    def setUp(self):
        self.num_string = '01-02-03-04-05'
        self.draw_date = '04/15/2013'

    def test_create(self):
        lotto_obj = models.lotto(self.num_string,self.draw_date)
        self.assertEqual(lotto_obj.get_game(),'Lotto')

    def test_get_numbers(self):
        lotto_obj = models.lotto(self.num_string,self.draw_date)
        self.assertEqual(lotto_obj.get_numbers(),['01','02','03','04','05'])

class powerball_model_test(unittest.TestCase, base_lotto_model_test):
    def setUp(self):
        self.num_string = '01-02-03-04-05[06]'
        self.draw_date = '04/15/2013'

    def test_create(self):
        powerball_obj = models.powerball(self.num_string,self.draw_date)
        self.assertEqual(powerball_obj.get_game(),'Powerball')

    def test_get_numbers(self):
        powerball_obj = models.powerball(self.num_string,self.draw_date)
        self.assertEqual(powerball_obj.get_numbers(),['01','02','03','04','05'])

    def test_get_powerball(self):
        powerball_obj = models.powerball(self.num_string,self.draw_date)
        self.assertEqual(powerball_obj.get_powerball(),'06');

class mega_millions_model_test(unittest.TestCase, base_lotto_model_test):
    def setUp(self):
        self.num_string = '01-02-03-04-05[06]'
        self.megaplier  = 'Megaplier: X4'
        self.draw_date  = '04/15/2013'

    def test_create(self):
        mega_obj = models.mega(self.num_string,self.draw_date)
        self.assertEqual(mega_obj.get_game(),'Mega Millions')

    def test_get_numbers(self):
        mega_obj = models.mega(self.num_string,self.draw_date)
        self.assertEqual(mega_obj.get_numbers(),['01','02','03','04','05'])

    def test_get_mega(self):
        mega_obj = models.mega(self.num_string,self.draw_date)
        self.assertEqual(mega_obj.get_mega(),'06');

    def test_get_megaplier(self):
        mega_obj = models.mega(self.num_string,self.draw_date)
        self.assertEqual(mega_obj.get_mega(),'4');


lotto_suite = unittest.TestLoader().loadTestsFromTestCase(lotto_model_test)
mega_suite  = unittest.TestLoader().loadTestsFromTestCase(mega_millions_model_test)
power_suite = unittest.TestLoader().loadTestsFromTestCase(powerball_model_test)

unittest.TextTestRunner(verbosity=2).run(lotto_suite)
unittest.TextTestRunner(verbosity=2).run(mega_suite)
unittest.TextTestRunner(verbosity=2).run(power_suite)
