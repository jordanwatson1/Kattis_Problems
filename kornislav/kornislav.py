#!/usr/bin/env python3

"""
Kattis: Kornislav
August 12, 2019

Description: Determine the largest rectangle the turtle can enclose
"""

import sys

integers = list(map(int, sys.stdin.readline().strip().split()))
integers.sort()
# The area is the multiplication of l * w
# thus the two sides facing each other will be divided into two groups
# by the two smallest numbers facing each other and the two
# largest numbers facing each other to maximize the area.
# Thus l * w is the smallest number of each group.
area = integers[0] * integers[2]
print(area)
