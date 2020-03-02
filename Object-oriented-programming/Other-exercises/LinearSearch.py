''' Question 2: Code with C# the method, which uses the linear search to find the element in the array. The
array contains 10000 random integers between 1-100000. Sort the array with the static Sort-method and try
to search some element '''
import random
import time

def search(arr, x):     # arr = some array | x = some element we want to find
  
    for i in range(len(arr)):   # Searching array one by one
  
        if arr[i] == x:     # If x is present then return its location 
            return i 
  
    return -1               # else return -1 

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

arr = []        # Making the array
for i in range(10000):
    arr.append(random.randint(1,100000))

num = 1203
arr.append(1203)
arr.sort()      # Sorting the arr
start_time1 = time.clock()
index = search(arr, num)    # Funct call
print("--- Linear Search : %s seconds ---" % (time.clock() - start_time1))

if index > 0:
    print(f'Found {num} at index {index}.')
else:
    print(f'{num} not found.')

start_time2 = time.clock()
# Function call 
result = binarySearch(arr, 0, len(arr)-1, num) 
print("--- Binary Search : %s seconds ---" % (time.clock() - start_time2))

if result != -1: 
    print("Element is present at index %d" % result)
else: 
    print("Element is not present in array")