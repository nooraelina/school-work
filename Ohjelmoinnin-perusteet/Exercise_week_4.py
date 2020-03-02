# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:13:12 2019

@author: noora
"""

# Tehtävä 1
def between():
    x = int(input('Give number '))
    a = int(input('Give second number '))
    b = int(input('Give third number '))
    if(a < x and x < b):
        print('{} is between second and third number'.format(x))
    elif (a > x and x > b):
        print('{} is between second and third number'.format(x))
    else:
        print('{} isn´t between second and third number'.format(x))
        
between()



# Tehtävä 2
def starts_with(word, char):
    """Checks if the name starts with char"""
    if ((word[0:len(char)]) == char):
        print( word + ' starts with '+ char)
    else:
        print(word + ' doesn´t start with' + char)

starts_with('sana','sa')
starts_with('sana','hfjshh')

# Tehtävä 3
def palindrome(word):
    if (word == ''.join(reversed(word))):
        print(word + ' is palindrome')
    else:
        print(word + ' is not palindrome')
        
palindrome('saippuakauppias')

# Tehtävä 4
def what_to_do():
    money = input('How much money do you have?')
    ticket = input('How much is the one-way bus ticket?')
    cinematicket = input('How much is the cinema ticket?')
    if (int(money) >= int(ticket) + int(ticket) + int(cinematicket)):
        print('You can go to the cinema and back with bus.')
    else:
        print('Stay home and watch some tv.')
        
what_to_do()
