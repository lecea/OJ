#!/usr/bin/python
# -*- coding: UTF-8 -*-
# input("按下 enter 键退出，其他任意键显示...\n")

# Fibonacci
a, b = 0, 1
while a < 10:
    print(a, end=',')
    a, b = b, a + b
