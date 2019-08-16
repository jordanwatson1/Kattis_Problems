#!/usr/bin/env python3

"""
Kattis: Oddities
August 15, 2019

Description: Determine if a number is odd or even
"""

import sys

cases = int(sys.stdin.readline().strip())

for i in range(cases):
    case = int(sys.stdin.readline().strip())
    if case % 2 == 0:
        print('%d is even' % case)
    else:
        print('%d is odd' % case)
