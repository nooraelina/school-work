# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:02:27 2019

@author: noora
"""

# Tehtävä 1
puhelinluettelo = {'name1':'0401234567',
                   'name2':'0401478523',
                   'name3':'0407896521'}
print(puhelinluettelo['name1'])

# Tehtävä 2
def sumUpTo(a):
    lista = [1,2,3,4,5]
    b = lista[:a]
    return sum(b)
    
print(sumUpTo(3))
print(sumUpTo(2))

# Tehtävä 3
def frame(width, length):
    a = width * '*'
    print(a)
    for i in range(length - 2):
        print('*', (width - 4) * ' ', '*')
    print(a)
    
frame(13,10)

# Tehtävä 4
def solve(legs,heads):
    print('Number of chickens: ')
    for chicks in range(0,heads):
        cows = heads - chicks
        totlegs = 4 * cows + 2 * chicks
        if totlegs == legs:
           return chicks
    return
    
print(solve(226,65))
