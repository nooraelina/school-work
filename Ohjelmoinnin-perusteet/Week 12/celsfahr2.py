# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 23:23:10 2019

@author: noora
"""

Cels_Fahr = {
        '20':68.0,
        '21':69.8,
        '22':71.6,
        '23':73.4,
        '24':75.2,
        '25':77.0,
        '26':78.8,
        '27':80.6,
        '28':82.4,
        '29':84.2
        }
def table():
    for key , value in Cels_Fahr.items():
        print(key, "  ", value)
