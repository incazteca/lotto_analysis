#!/usr/bin/env python

from datetime import date

class lotto:
    def __init__(self,tot_num,nums,draw_date):
        self.game = self.__class__.__name__
        self.total_numbers = tot_num
        self.numbers = list(nums)

        # Ensure that the draw date is a date object
        self.draw_date = draw_date

    # Accesors
    def get_nums():
        return self.nums

    def get_draw_date():
        return self.draw_date
