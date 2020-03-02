# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:31:16 2019

@author: noora
"""
# Tehtävä 1
def infinite(*args):
    summa = 0
    for numero in args:
        summa = summa + numero
    print(summa / len(args))
        
infinite(7,3,57)
infinite(45,32,2362,25,46,34)

# Tehtävä 2
def withspace(text):
    sana = '\t'.join(text)
    print(sana)
    
withspace(input('Word:'))

# Tehtävä 3
import random
def dice():
    return random.randint(1,7)

while dice() != 6:
    print('Muu kuin 6.')
print('6.')

# Tehtävä 4
def fancy_print(sana):
    counter = 1
    for kirjain in sana:
        print(sana[0:counter])
        counter += 1
        
fancy_print('qwert')