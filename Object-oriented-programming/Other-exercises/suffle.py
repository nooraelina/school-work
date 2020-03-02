
from random import randint, random
from math import floor

def fisher_yates_shuffle(the_list):
    list_range = range(0, len(the_list))
    for i in list_range:
        j = randint(list_range[0], list_range[-1])
        the_list[i], the_list[j] = the_list[j], the_list[i]
        print(the_list)
    return the_list

theList = ['Moomintroll', 'Snorkmaiden', 'Little My', 'Snufkin', 'Sniff', 'Stinky']
a = fisher_yates_shuffle(theList)
print(a)