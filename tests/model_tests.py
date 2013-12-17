#!/usr/bin/env python
"""
Unit Test for lotto model in models.py
"""
import sys
import unittest
import inspect

sys.path[0:0] = [""]
from lotto_analysis import models

"""
    Test for lotto game. Sample input from
    http://www.illinoislottery.com/lottery/data/history/winners/all/pastYear.json

    sample json input:
    {
        "col1": "04/15/2013",
        "col2": "Lotto",
        "col3": [
            "02-04-08-20-21-47, Extra Shot : 06",
            " "
        ],
        "col4": "",
        "col5": ""
    }
"""
class lotto_model_test(unittest.TestCase):
    def setUp(self):
        self.game = 'Lotto'
        self.num_string = '02-04-08-20-21-47, Extra Shot : 06'
        self.draw_date = '04/15/2013'

    def test_create(self):
        lotto_obj = models.lotto(self.game, self.num_string, self.draw_date)
        self.assertEqual(lotto_obj.get_game(),'Lotto')

    def test_get_numbers(self):
        lotto_obj = models.lotto(self.game, self.num_string, self.draw_date)
        self.assertEqual(lotto_obj.get_numbers(),['02','04','08','20','21','47'])

    def test_get_extra_shot(self):
        lotto_obj = models.lotto(self.game, self.num_string, self.draw_date)
        self.assertEqual(lotto_obj.get_extra_shot(),'06');

    def test_get_draw_date(self):
        lotto_obj = models.lotto(self.game, self.num_string, self.draw_date)

        # Ensure that draw_date is a date object
        self.assertEqual(lotto_obj.get_draw_date().year,2013)
        self.assertEqual(lotto_obj.get_draw_date().month,4)
        self.assertEqual(lotto_obj.get_draw_date().day,15)

"""
    Test for powerball game. Sample input from
    http://www.illinoislottery.com/lottery/data/history/winners/all/pastYear.json

    sample json input:
    {
        "col1": "04/13/2013",
        "col2": "Powerball",
        "col3": [
            "10-12-31-56-57[33]",
            " "
        ],
        "col4": "",
        "col5": ""
    }
"""
class powerball_model_test(unittest.TestCase):
    def setUp(self):
        self.game = 'Powerball'
        self.num_string = '10-12-31-56-57[33]'
        self.draw_date = '04/13/2013'
        self.day = 13

    def test_create(self):
        powerball_obj = models.powerball(self.game, self.num_string, self.draw_date)
        self.assertEqual(powerball_obj.get_game(),'Powerball')

    def test_get_numbers(self):
        powerball_obj = models.powerball(self.game, self.num_string, self.draw_date)
        self.assertEqual(powerball_obj.get_numbers(),['10','12','31','56','57'])

    def test_get_powerball(self):
        powerball_obj = models.powerball(self.game, self.num_string, self.draw_date)
        self.assertEqual(powerball_obj.get_powerball(),'33');

    def test_get_draw_date(self):
        powerball_obj = models.powerball(self.game, self.num_string, self.draw_date)

        # Ensure that draw_date is a date object
        self.assertEqual(powerball_obj.get_draw_date().year,2013)
        self.assertEqual(powerball_obj.get_draw_date().month,4)
        self.assertEqual(powerball_obj.get_draw_date().day,13)

"""
    Test for megamillions game. Sample input from
    http://www.illinoislottery.com/lottery/data/history/winners/all/pastYear.json

    {
        "col1": "04/09/2013",
        "col2": "Mega Millions",
        "col3": [
            "17-30-41-48-54[13]",
            ", Megaplier: X4"
        ],
        "col4": "",
        "col5": ""
    }
"""
class mega_millions_model_test(unittest.TestCase):
    def setUp(self):
        self.game = 'Mega Millions'
        self.num_string = '17-30-41-48-54[13]'
        self.megaplier  = ', Megaplier: X4'
        self.draw_date  = '04/09/2013'

    def test_create(self):
        mega_obj = models.mega_millions(self.game, self.num_string, self.megaplier, self.draw_date)
        self.assertEqual(mega_obj.get_game(),'Mega Millions')

    def test_get_numbers(self):
        mega_obj = models.mega_millions(self.game, self.num_string, self.megaplier, self.draw_date)
        self.assertEqual(mega_obj.get_numbers(),['17','30','41','48','54'])

    def test_get_mega(self):
        mega_obj = models.mega_millions(self.game, self.num_string, self.megaplier, self.draw_date)
        self.assertEqual(mega_obj.get_mega(),'13');

    def test_get_megaplier(self):
        mega_obj = models.mega_millions(self.game, self.num_string, self.megaplier, self.draw_date)
        self.assertEqual(mega_obj.get_megaplier(),'4');

    def test_get_draw_date(self):
        mega_obj = models.mega_millions(self.game, self.num_string, self.megaplier, self.draw_date)

        # Ensure that draw_date is a date object
        self.assertEqual(mega_obj.get_draw_date().year,2013)
        self.assertEqual(mega_obj.get_draw_date().month,4)
        self.assertEqual(mega_obj.get_draw_date().day,9)

# Set up testing suites

lotto_suite = unittest.TestLoader().loadTestsFromTestCase(lotto_model_test)
mega_suite  = unittest.TestLoader().loadTestsFromTestCase(mega_millions_model_test)
power_suite = unittest.TestLoader().loadTestsFromTestCase(powerball_model_test)

print "-------------COMMENCE TESTING------------"

print "-----------COMMENCE LOTTO TESTING--------"
unittest.TextTestRunner(verbosity=2).run(lotto_suite)

print "------COMMENCE MEGA MILLIONS TESTING-----"
unittest.TextTestRunner(verbosity=2).run(mega_suite)

print "--------COMMENCE POWERBALL TESTING-------"
unittest.TextTestRunner(verbosity=2).run(power_suite)
