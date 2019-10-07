#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import test2
import builtins
# if __name__ == "__main__":
    # print(sys.path)
    # print(dir(test2))
    # print(dir(sys))
    # print(dir())
    # print(dir(builtins))
    # yes_votes = 42_572_654
    # no_votes = 43_132_495
    # percentage = yes_votes / (yes_votes + no_votes)
    # print(percentage)
    # print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
    # x = 10 * 3.25
    # y = 200 * 200
    # s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
    # print(s)

    # for x in range(1, 11):
    #     print(repr(x).rjust(2), repr(x * x).rjust(3), repr(x * x * x).rjust(4))


# def f(a, b):
#     if b == 0:
#         print(a)
#     else:
#         f(b, a%b)
# a, b = input("Enter two natural numbers: ")
# print(f(a, b))

# class Person:
#     def __init__(self):
#         pass
#
#     def getAge(self):
#         print(__name__)
#
#
# p = Person()
# p.getAge()

# import math
# def sieve(size):
#     sieve= [True] * size
#     sieve[0] = False
#     sieve[1] = False
#     for i in range(2, int(math.sqrt(size)) + 1):
#         k= i * 2
#         while k < size:
#            sieve[k] = False
#            k += i
#     return sum(1 for x in sieve if x)
# print(sieve(10000000000))

x = True
y = False
z = False

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)