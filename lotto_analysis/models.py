#!/usr/bin/env python
"""
    Document contains the models for the different lotto games
"""
from datetime import date

"""
    Class for lotto game model. Also base class for other permutations of the game
"""
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

"""
    Class for little lotto game model.
"""
class little_lotto(lotto):
    def __init__(self,num_string,draw_date):
        self.game = 'Little Lotto'

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

"""
    Class for mega millions game model.
"""
class mega_millions(lotto):
    def __init__(self,num_string,draw_date):
        self.game = 'Mega Millions'

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

"""
    Class for Powerball game model.
"""
class powerball(lotto):
    def __init__(self,num_string,draw_date):
        self.game = 'Powerball'

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

"""
    Class for Pick 3 game model.
"""
class pick_3(lotto):
    def __init__(self,num_string,draw_date):
        self.game = 'Pick 3'

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

"""
    Class for Pick 4 game model.
"""
class pick_4(lotto):
    def __init__(self,num_string,draw_date):
        self.game = 'Pick 4'

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
