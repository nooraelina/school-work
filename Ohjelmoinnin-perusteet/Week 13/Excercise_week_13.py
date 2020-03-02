# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:45:10 2019

@author: noora
"""

class Clock:    # t. 1
    hours = 00      # attribute: hours
    minutes = 00    # attribute: minutes
    
class Dog:  # t. 2
    def __init__(self, name, age, is_inoculated):
        self.name = name
        self.age = age
        self.is_inoculated = is_inoculated
    def printtaa(self):
        print('Koiran nimi: ',self.name,'and age ',self.age,'. Is dog inoculated?',self.is_inoculated)
    def bark(self):     # liittyen t. 4.
        print('wuff wuff')

class Complex_number:   # t. 3
    a = 0    # real part
    b = 0    # imaginary part
    def __init__(self, a, b):
        self.a = a
        self.b = b

def add_complex(complexNumber1,complexNumber2):
    x = complexNumber1.a + complexNumber2.a
    y = complexNumber1.b + complexNumber2.b
    return ('{0} + {1}i'.format(x,y))

class Police_dog(Dog):
    status = 'high'
    def bark(self):
        print('bouuuuw')

def main():
    ''' Tehtävä 1 '''
    clock1 = Clock()
    clock1.hours = 5
    clock1.minutes = 14
    print(clock1.hours,':',clock1.minutes)
    ''' Tehtävä 2 '''
    dog1 = Dog('Puppe',7,'Yes')
    dog2 = Dog('Miisa',4,'Yes')
    dog1.printtaa()
    dog2.printtaa()
    ''' Tehtävä 3 '''
    nro1 = Complex_number(4,6)
    nro2 = Complex_number(2,7)
    print(add_complex(nro1,nro2))
    ''' Tehtävä 4 '''
    dog1.bark()
    police_dog1 = Police_dog('Rocky',11,True)   # Luodaan poliisikoira
    police_dog1.bark()

main()

