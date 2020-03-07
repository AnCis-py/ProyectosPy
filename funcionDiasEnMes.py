# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:50:36 2020

@author: CEC
"""

def isYearLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True 
            else:
                return False 
        else:
            return True
    else:
        return False
    
def daysInMonth(year, month):
    if month == 4 or month == 6 or
