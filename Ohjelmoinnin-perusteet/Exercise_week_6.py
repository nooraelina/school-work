# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 15:14:16 2019

@author: noora
"""

# Tehtävä 1 Calculate the middle point of the word and return the corresponding letter.
def middle2(word):
    number = (len(word)+1)/2
    if (number == int(number)):
        print(word[int(number -1)])
    else:
        print('The word doesn´t have middle letter')
        
middle2('qwer')
middle2('qwert')

# Tehtävä 2 
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
for key , value in Cels_Fahr.items():
    print(key, "  ", value)

# Tehtävä 3
newlist = [ 2 ** x for x in range(11)]
print(newlist)

# Tehtävä 4
multipliers = [7,3,1,7,3,1,7,3,1,7,3,1,7,3,1,7,3,1,7]
def refnumber(list):
    # Multiply
    backWardsList = list[::-1]
    multis = [multipliers*backWardsList for multipliers,backWardsList in zip(multipliers,backWardsList)]
    # Sum up multis
    sum_multis = sum(multis)
    # Substract from the following ten
    # result is the checksum  
    sum_multis2 = sum_multis
    while (sum_multis % 10 != 0):
        sum_multis = sum_multis +1
    checksum = (sum_multis - sum_multis2)
    print('Reference number is', end=' ')
    for x in list:
        print(x, end='')
    print(checksum)
    list.append(checksum)
    return list
        
list1 = [4,5,4,8,7,5,7,6]
list2 = [5,1,5,4,8,4,1,7,5]
refnumber(list1)
refnumber(list2)
refnumber([1,2,3,4,5,6])
