# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:35:17 2019

@author: noora
"""
import math
# Tehtävä 1
def average(*args):
    if len(args) == 0:
        return ('no parameters given')
    else:
        return sum(args) / len(args)
print(average(12))
print(average())

# Tehtävä 2
def average2(*args):
    try:
        return sum(args) / len(args)
    except Exception:
        return ('No parameters given')
print(average2(3,5))
print(average2())

# Tehtävä 3
def read_file(fname):
    try:
        f = open(fname)
    except (NameError, TypeError, Exception):
        return ('Error')
    else:
        string = f.read()
        f.close()
        return string
print(read_file('somefile'))
try:
    print(read_file())
except Exception:
    print('no parametres')

# Tehtävä 4
def solve():
    try:
        print('Solve the second order equation ax^2 + bx + c = 0 by giving a, b and c')
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))
    except Exception:
        print('Error')
        return
    else:
        diskr = b*b - 4*a*c
        if diskr > 0:
            x1 = (-b + math.sqrt(diskr)) / 2*a
            x2 = (-b - math.sqrt(diskr)) / 2*a
            print('x = ', x1, 'or x = ', x2)
        if diskr == 0:
            x12 = -(b / 2*a)
            print('x = ', x12)
        if diskr < 0:
            print('no real roots')
solve()