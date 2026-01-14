#say that you have several lists of numbers and 
# want to calculate the square of each number 
# in all lists. You can use chain() as follows:

from itertools import chain

first = [7, 6, 1]
second = [4, 1]
third = [8, 0, 6]

for value in chain(first, second, third):
    print(value**2)


#Say that you, again, need to process each 
# value in a sequence and calculate its square:

#FOR MATRIX

matrix = [
    [9, 3, 8],
    [4, 5, 2],
    [6, 4, 3],
]

for value in chain(*matrix):
    print(value**2)

