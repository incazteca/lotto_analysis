#!/usr/bin/env python
"""
    Document contains the models for the different lotto games
"""
from datetime import date

#---------------------------------------------------- Class for lotto game model

class lotto:
    def __init__(self,num_string,draw_date):
        self.game = 'Lotto'

        # Parse numbers string create list of numbers
        
        self.numbers = num_string.split('-')
        
        # Ensure that the draw date is a date object. Y-M-D
        date_ar = draw_date.split('/')
        self.draw_date = date(int(date_ar[2]),int(date_ar[0]),int(date_ar[1]))

    # Accesors
    def get_game(self):
        return self.game

    def get_numbers(self):
        return self.numbers

    def get_draw_date(self):
        return self.draw_date

#---------------------------------------------------- Class for little lotto game model
class little_lotto(lotto):
    pass
#---------------------------------------------------- Class for mega millions game model
class mega_millions(lotto):
    pass
#---------------------------------------------------- Class for powerball game model
class powerball(lotto):
    pass
#---------------------------------------------------- Class for pick 3 game model
class pick_3(lotto):
    pass
#---------------------------------------------------- Class for pick 4 game model
class pick_4(lotto):
    pass
