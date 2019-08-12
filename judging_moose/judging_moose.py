#!/usr/bin/env python3

"""
Kattis: Judging Moose
August 12, 2019

Description: Determine the total number of tines(sharp points) a moose has
"""

import sys

tines = tuple(map(int, sys.stdin.readline().strip().split()))

if tines[0] == 0 and tines[1] == 0:
    print('Not a moose')
elif tines[0] == tines[1]:
    print('Even {}'.format(tines[0] * 2))
elif tines[0] > tines[1]:
    print('Odd {}'.format(tines[0] * 2))
else:
    print('Odd {}'.format(tines[1] * 2))
