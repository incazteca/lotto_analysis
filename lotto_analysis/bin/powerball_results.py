#!/usr/bin/env python

import json
import sys

from lotto_analysis import models
from lotto_analysis import factories

game_type = 'Powerball'

lotto_fact = factories.lotto_factory(game_type);
power_ar = lotto_fact.retrieve_powerball();

list_format = "{!s:15}{!s:10}{!s:10}{!s:10}"
print list_format.format('Date','Game','Numbers','Powerball')

counter = 0
for power in power_ar:
    if counter % 25 == 0:
        print list_format.format('Date','Game','Numbers','Powerball')
        print '-'*45
    print list_format.format(power.get_draw_date(),power.get_game()," ".join(power.get_numbers()), " ".join(power.get_powerball()))
    counter +=1
