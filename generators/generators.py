'''
>>> evens = evens_up_to(8)
>>> type(evens)
<class 'generator'>
>>> for even in evens:
...     print(even)
2
4
6
8

>>> squares = squares_up_to(16)
>>> type(squares)
<class 'generator'>
>>> for square in squares:
...     print(square)
1
4
9
16

>>> for square in squares_up_to(15):
...     print(square)
1
4
9

>>> counter = countdown(3)
>>> type(counter)
<class 'generator'>
>>> for count in countdown(3):
...     print(count)
3
2
1
BLASTOFF!

>>> for count in countdown(10):
...     print(count)
10
9
8
7
6
5
4
3
2
1
BLASTOFF!

'''

# Write your code here:

def evens_up_to(max_base):
    n = 2
    while n <= max_base:
        yield  n
        n += 2

def squares_up_to(limit):
    n = 1
    square = n ** 2
    while square <= limit:
        yield square
        n += 1
        square = n ** 2

def countdown(max):
    n = max
    while n > 0:
        yield n
        n -= 1
    yield "BLASTOFF!"

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2016 Aaron Maxwell. All rights reserved.
