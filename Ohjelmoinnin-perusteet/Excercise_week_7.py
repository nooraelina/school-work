# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 12:22:57 2019

@author: noora
"""

# Tehtävä 1
def initials():
    x = input('Give first name: ')
    y = input('Give last name: ')
    print(x[0],y[0],sep='.',end='.')
initials()

# Tehtävä 2
import random
dice = [random.randint(1,7) for i in range(6)]
print(dice)

# Tehtävä 3
def lista(*args):
    list = []
    n = int(input('How many numbers do you want in a list? '))
    for i in range(0,n):
        x = int(input())
        list.append(x)
    print(list)
lista()

# Tehtävä 4
def first_letters(*args):
    print('First give the length of list, press enter, then type same amount of words pressing enter after each one.')
    list = []
    n = int(input('Length of list '))
    for i in range(0,n):
        x = input()
        list.append(x)
    list2 = [x[0] for x in list]
    print(list2)
first_letters()

# Tehtävä 5
import random
lottery = []
while len(lottery) < 7:
    x = [random.randint(1,40)]
    if lottery.__contains__(x):
        continue
    else:
        lottery.append(x)
print(lottery)