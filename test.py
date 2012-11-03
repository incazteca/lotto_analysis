#!/usr/bin/env python

import json
import sys
import lib.models.lotto
import lib.factories.lotto

numbers = [3,2,4]

lotto_obj = lib.models.lotto.lotto(3,numbers,'20120623')

print lotto_obj.game
print lotto_obj.numbers

print "-"*5
print "Test Factories"
print "-"*5

lotto_fact = lib.factories.lotto.lotto_factory('lotto');
lot_json = lotto_fact.retrieve_lotto('lotto');

print lot_json

#print json.dumps(lot_json)
