#!/usr/bin/env python

"""
this is test pydoc
"""

import json
import sys
sys.path[0:0] = [""]

from lotto_analysis import models
from lotto_analysis import factories

print "-"*5
print "Test Factories"
print "-"*5

lotto_fact = factories.lotto_factory('Lotto');
#lot_json = lotto_fact.retrieve_lotto('Lotto');
lot_ar = lotto_fact.retrieve_lotto();

list_format = "{!s:15}{!s:10}{!s:10}"
print list_format.format('Date','Game','Numbers')

counter = 0
for lot in lot_ar:
    if counter % 25 == 0:
        print list_format.format('Date','Game','Numbers')
        print '-'*35
    print list_format.format(lot.get_draw_date(),lot.get_game()," ".join(lot.get_numbers()))
    counter +=1
