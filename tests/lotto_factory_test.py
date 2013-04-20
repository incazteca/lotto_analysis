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
        pass

    def retrieve_lotto_game(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(lotto_factory_test)
unittest.TextTestRunner(verbosity=2).run(suite)
