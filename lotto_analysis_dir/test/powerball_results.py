#!/usr/bin/env python

import json
import sys
import lib.models.lotto
import lib.factories.lotto

game_type = 'Powerball'

lotto_fact = lib.factories.lotto.lotto_factory(game_type);
lot_json = lotto_fact.retrieve_lotto(game_type);

list_format = "{!s:15}{!s:10}{!s:10}"
print list_format.format('Date','Game','Numbers')

for lot in lot_json:
    print list_format.format(lot['col1'],lot['col2'],lot['col3'])
