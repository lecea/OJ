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

words = ['cat', 'window', 'defenestrate']
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print(words)
