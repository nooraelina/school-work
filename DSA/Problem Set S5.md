## Problem Set S5

Question 1: We have a sequence 2,4,6,7,8,9,11,14,21,28,33,35,39. Test, if the sequence has the element 12 by using Binary Search.
```
# Iterative Binary Search Function 
# If x is found in arr: returns x´s index number
# else: returns -1 
def binarySearch(arr, l, r, x): 
  
    while l <= r: 
        mid = int(l + (r - l)/2)           
        if arr[mid] == x:   # Checking is x in mid
            return mid 
        elif arr[mid] < x:  # x is greater: ignore left part
            l = mid + 1
        else:               # x is smaller: ignore right part
            r = mid - 1
    # If we reach here, then the element was not present 
    return -1

arr = [2,4,6,7,8,9,11,14,21,28,33,35,39]    # Tested array
x = 12
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
    print("Element is present at index %d" % result)
else: 
    print("Element is not present in array")
```
OUTPUT: Element is not present in array
Array doesn´t have the element.


Question 2: Code with C# the method, which uses the linear search to find the element in the array. The array contains 10000 random integers between 1-100000. Sort the array with the static Sort-method and try to search some element.
import random
```
def search(arr, x):     # arr = some array | x = some element we want to find
  
    for i in range(len(arr)):   # Searching array one by one
  
        if arr[i] == x:     # If x is present then return its location 
            return i 
  
    return -1               # else return -1 

arr = []        # Making the array
for i in range(10000):
    arr.append(random.randint(1,100000))

num = 1203
arr.sort()      # Sorting the arr
index = search(arr, num)    # Funct call
if index > 0:
    print(f'Found {num} at index {index}.')
else:
    print(f'{num} not found.')
```

Question 5: Use the shuffling algorithm of the material to shuffle the names {“Moomintroll”, “Snorkmaiden”, “Little My”, “Snufkin”, “Sniff”, “Stinky”}
Question 6: Code the shuffling algorithm of the material with C# and test it.
Q5&Q6 both:
```
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
```
OUTPUT:

['Snorkmaiden', 'Moomintroll', 'Little My', 'Snufkin', 'Sniff', 'Stinky']

['Snorkmaiden', 'Sniff', 'Little My', 'Snufkin', 'Moomintroll', 'Stinky']

['Snorkmaiden', 'Sniff', 'Snufkin', 'Little My', 'Moomintroll', 'Stinky']

['Snorkmaiden', 'Sniff', 'Snufkin', 'Stinky', 'Moomintroll', 'Little My']

['Moomintroll', 'Sniff', 'Snufkin', 'Stinky', 'Snorkmaiden', 'Little My']

['Moomintroll', 'Sniff', 'Little My', 'Stinky', 'Snorkmaiden', 'Snufkin']

['Moomintroll', 'Sniff', 'Little My', 'Stinky', 'Snorkmaiden', 'Snufkin'] <-This is the suffled list, a.
