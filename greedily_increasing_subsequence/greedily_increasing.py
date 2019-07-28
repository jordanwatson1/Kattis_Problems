#!/usr/bin/env python3

"""
Kattis: Greedily Increasing Subsequence
July 28, 2019
"""

import sys

num_elements = int(sys.stdin.readline().strip())

permutations = list(map(int, sys.stdin.readline().strip().split()))
GIS = []

prev = permutations[0]
GIS.append(prev)

for i in permutations:
	if i > prev:
		GIS.append(i)
		prev = i

s = [str(i) for i in GIS]

print(len(GIS))
print(' '.join(s))