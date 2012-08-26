#!/usr/bin/env python

import sys
import lib.models.lotto

numbers = [3,2,4]

lotto_obj = lib.models.lotto.lotto(3,numbers,'20120623')

print lotto_obj.game
print lotto_obj.numbers
