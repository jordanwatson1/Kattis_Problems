#!/usr/bin/env python3

"""
Kattis: Mirror Images
July 25, 2019
"""

import sys

num_cases = int(sys.stdin.readline().strip())

i = 1
while i <= num_cases:
	print("Test" + ' ' + str(i))
	i += 1

	row_col = tuple(map(int, sys.stdin.readline().strip().split()))
	li = []
	for row in range(row_col[0]):
		img = sys.stdin.readline().strip()
		img = img[::-1]
		li.append(img)

	li.reverse()
	for item in li:
			print(item)