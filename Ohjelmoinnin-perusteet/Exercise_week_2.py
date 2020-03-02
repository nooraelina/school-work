# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 12:23:21 2019

@author: noora
"""
# Tehtävä 1
def t1(firstName):
    return 'Hello {}!'.format(firstName)

print('Anna nimesi: ')
etunimi = input()
print(t1(etunimi))

# Tehtävä 2
someword = 'mickey'

def word():
    print(someword[0])

word()

# Tehtävä 3
def velocity():
    distance = 168
    time = 2 + 1/6
    return float(distance / time)

print(velocity())

# Tehtävä 4
bmi_info = ('''BMI = Body Mass Index
            Below 19 = underweight
            19-25 = normal
            25-30 = overweight
            30+ = obese''')

def bmi():
    w = float(input('Give your weight:'))
    h = float(input('Give your height:'))
    print(bmi_info)
    print('Your BMI:')
    print((w / (h * h) ) * 10000)

bmi()

# Tehtävä 5
def average():
    print('Give a number:')
    x = float(input())
    print('Give second number:')
    y = float(input())
    print('Give third number:')
    z = float(input())
    print((x + y + z)/3)

average()

