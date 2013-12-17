"""
    Document contains the models for the different lotto games
"""
from datetime import date
import re

"""
    Base lotto class
"""
class base_lotto(object):
    def __init__(self, game, num_string, draw_date):
        self.game = game

        # Parse numbers string create list of numbers
        self.numbers = self.parse_numbers(num_string)

        # Ensure that the draw date is a date object. Y-M-D, 2013-12-30
        date_ar = draw_date.split('/')
        self.draw_date = date(int(date_ar[2]),int(date_ar[0]),int(date_ar[1]))

    def parse_numbers(self,nums):
        num_parts = nums.split(',')
        return num_parts[0].split('-')

    # Accessors
    def get_game(self):
        return self.game

    def get_numbers(self):
        return self.numbers

    def get_draw_date(self):
        return self.draw_date

"""
    Class for lotto game model
"""
class lotto(base_lotto):
    def __init__(self, game, num_string, draw_date):
        super(lotto,self).__init__(game, num_string, draw_date)

        pot_extra_shot = num_string.split(',')[1]

        if ( pot_extra_shot != ''):
            self.extra_shot = pot_extra_shot.split(':')[-1].strip()
        else:
            self.extra_shot = ''

    def get_extra_shot(self):
        return self.extra_shot

"""
    Class for mega millions game model.
"""
class mega_millions(base_lotto):
    def __init__(self, game, num_string, megaplier, draw_date):
        super(mega_millions,self).__init__(game, num_string, draw_date)

        # Parse numbers string create list of numbers and get mega number

        self.numbers = num_string.split('-')
        last_elem = self.numbers[-1].split('[')
        self.numbers[-1] = last_elem[0]
        self.mega = last_elem[1][:-1]

        # Retrieve megaplier, use regex to find megaplier digit
        megaplier_temp = megaplier.split(':')[-1];

        re_handle = re.compile('(\d)')
        self.megaplier = re_handle.search(megaplier_temp).group(1)

    # Accesors
    def get_mega(self):
        return self.mega

    def get_megaplier(self):
        return self.megaplier

"""
    Class for Powerball game model.
"""
class powerball(base_lotto):
    def __init__(self, game, num_string, draw_date):
        super(powerball,self).__init__(game, num_string, draw_date)


        # Parse numbers string create list of numbers

        self.numbers = num_string.split('-')
        last_elem = self.numbers[-1].split('[')
        self.numbers[-1] = last_elem[0]
        self.powerball = last_elem[1][:-1]

    # Accesors
    def get_powerball(self):
        return self.powerball
