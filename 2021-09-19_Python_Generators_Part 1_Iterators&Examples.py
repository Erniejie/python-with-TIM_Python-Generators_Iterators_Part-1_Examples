#Python Generators Explained
#Tech With Tim_yt- Aug 3,2021

#Part 1:Iterators

import sys

#Example 7: Creating Legacy Iterators
"Example 7: Making your own iterator using old legacy syntaxis "

class Iter:
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1

        if self.current >= self.n:
            raise StopIteration

        return self.current

x = Iter(19)

#for i in x:
#    print(i)

itr = iter(x)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))





"""
"Example 6:  iterator using <iter> function "

x = range(1,13)

print(next(iter(x)))

"""
    



"""
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


