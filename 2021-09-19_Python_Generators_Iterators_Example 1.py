#Python Generators Explained
#Tech With Tim_yt- Aug 3,2021

#Part 1:

import sys

"Example 5:  iterator for loop = iterator while loop"

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]  # list

y = map(lambda i: i**2,x)


#A:For Loop
for i in y:
    print(i)

#B: While Loop
while True:
    try:
        value = next(y)
        print(value)
    except StopIteration:
        print("Done")
        break

# A == B






"""
"Example 4:  Example 3 using dunder methods(doubleunderscore)"

x = [1,2,3,4,5,6,7,8,9,10,11]  # list

y = map(lambda i: i**2,x)

print(y.__next__())

print("For Loop starts from here:")
for i in y:
    print(i)
"""





""""
"Example 3: How an Iterator works:"

x = [1,2,3,4,5,6,7,8,9,10,11]  # list

y = map(lambda i: i**2,x)

# special function : next
print(next(y))
print(next(y))
print(next(y))
print(next(y))

print("For Loop starts from here:")
for i in y:
    print(i)
"""
    


"""
"Example 2: for loop- NO storying the sequence"

x = [1,2,3,4,5,6,7,8,9,10,11]  # list

y = map(lambda i: i**2,x)

for i in y:
    print(i)
"""


"""
"Example 1: no loop- storing  the sequence"

x = [1,2,3,4,5,6,7,8,9,10,11]  # list

y = map(lambda i: i**2,x)

print(list(y))
"""


