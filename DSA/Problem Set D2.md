1.
```
def hi_recursive(remaining):  
    # The base case
    if remaining == 0:
        return
    print(remaining)
    # Call to function, with a reduced remaining count
    hi_recursive(remaining - 1)
hi_recursive(7)
```
2. 
```
def hi_recursive(n):  
    if n != 0:
        hi_recursive(n - 1)
    print(n)
hi_recursive(7)
```
3.
```
def hi_iteration(x, n):
    count = 2
    y = x
    while count <= n:
        count += 1
        y *= x
    print(y)
hi_iteration(3, 7)
```
4.
```
def recursive1(x, n):
    if n == 0:
        n = 1
        recursive1(x, n)
    if n > 0:
        ans = x * (x**(n-1))
        print(ans)
    if n < 0:
        ans = (n**(n+1))/x
        print(ans)

recursive1(3, 3)
recursive1(3, -3)
recursive1(3, 0)
```
6.
```
def reversestr(somestr):
    if len(somestr) == 0: 
        return
    temp = somestr[0] 
    reversestr(somestr[1:]) 
    print(temp, end='')
string1 = ("Let's reverse this string.")
reversestr(string1)
```
7. 
```
# Iterative
myList = [1,3,5,7,9]
def iter(numList):
    sum = 0
    for i in numList:
        sum = sum + i
    print(sum)
    return sum
iter(myList)

# Recursive
def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))
```
8.
```
def toBinary(n):
    remStack = []
    while n > 0:
        rem = n % 2
        remStack.append(rem)
        n = n // 2
    binStr = ""
    while not len(remStack) == 0:
        binStr +=str(remStack.pop())
    return binStr

print(toBinary(42))
```
BONUS
9.
```
def hanoi(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)
        
source = [3,2,1]
target = []
helper = []
hanoi(len(source),source,helper,target)

print(source, helper, target)
```
10.
```
def rows(n1, n2):
    if n1 == n2:
        return
    writeFromZeroTo(n2)
    rows(n1, n2 + 1)
    writeFromZeroTo(n2 - 1)

def writeFromZeroTo(n2):
    for i in range(n2):
        print("{} ".format(i), end = " ")
    print()
    return

rows(5, 1)
```