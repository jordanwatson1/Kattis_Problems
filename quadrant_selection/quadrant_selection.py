#!/usr/bin/env python3

"""
Kattis: Quadrant Selection
August 18, 2019

Description: Given a point on a grid, determine which quadrant the point is in.
(−1000 <= x, y <= 1000; x != 0)
"""

import sys

x = int(sys.stdin.readline().strip())
y = int(sys.stdin.readline().strip())

if x > 0 and y > 0: print(1)
elif x < 0 and y > 0: print(2)
elif x < 0 and y < 0: print(3)
else: print(4)
