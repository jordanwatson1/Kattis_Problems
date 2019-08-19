#!/usr/bin/env python3

"""
Kattis: Ragged Right
August 19, 2019

Description: Calculate the raggedness of a paragraph.
"""

import sys

p = sys.stdin.read().split('\n')
n = 0

for line in p:
    if len(line) > n:
        n = len(line)

raggedness = [(n - len(m))**2 for m in p[:-2]]
print(sum(raggedness))
