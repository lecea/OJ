#!/usr/bin/python
# -*- coding: UTF-8 -*-

# x = int(input())
# if x < 0:
#     x = -x
# elif x == 0:
#     x = 0
# else:
#     x = x
#
# print(x)

# words = ['cat', 'window', 'defenestrate']
# for w in words[:]:
#     if len(w) > 6:
#         words.insert(0, w)
# print(words)
# for i in range(len(words)):
#     print(i+1, words[i])

# list(range(5))
# print(list(range(5)))

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             break
#     else:
#         print(n)
# the else clause belongs to the for loop, not the if statement.)

# def fib(n):
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         # print(a, end=' ')
#         a, b = b, a + b
#     return result
#
# # f = fib
# # f(200)
# print(fib(100))


# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
#
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)

# i = 5
#
# def f(arg=i):
#     print(arg)
#
# i = 6
# f()

# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L
# print(f(1))
# print(f(2))
# print(f(3))

# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
#
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])
#
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

# def concat(*args, sep="/"):
#     return sep.join(args)
#
# print(concat("earth", "mars", "venus"))
#
# str = "aaaaa"
# str2 = str.join("/")
# print(str2)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print([num for elem in vec for num in elem])

# print(list(zip(*matrix)))

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print("what is your {0}? It is {1}.".format(q, a))






