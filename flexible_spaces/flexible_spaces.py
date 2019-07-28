#!/usr/bin/env python3

"""
Kattis: Flexible Spaces
July 28, 2019
"""

import sys

w_and_numP = list(map(int, sys.stdin.readline().strip().split()))
partitions = list(map(int, sys.stdin.readline().strip().split()))

spaces = []
li = []
li.append(0)
li.extend(partitions)
li.append(w_and_numP[0])

for index, i in enumerate(li, start=1):
	for j in li[index:]:
		val = j - i
		spaces.append(val)

spaces.sort()

print(spaces[0])
prev = spaces[0]

for i in spaces[1:]:
	if i != prev:
		print(i)
	prev = i
