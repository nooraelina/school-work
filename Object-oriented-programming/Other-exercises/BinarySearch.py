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