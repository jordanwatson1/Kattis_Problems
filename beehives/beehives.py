#!/usr/bin/env python3

"""
Kattis: Beehives
July 17, 2019
"""

import sys
import math

def sweet_or_sour(d, li):
	sour = 0
	sweet = 0
	for x in li:
		min_len = 1000
		
		for y in li:
			base = abs(x[0] - y[0])
			height = abs(x[1] - y[1])
			length = math.sqrt(math.pow(base, 2) + math.pow(height, 2))
			
			if length != 0.0 and length < min_len:
				min_len = length

		if min_len < d:
			sour += 1
		else:
			sweet += 1

	return (str(sour) + " sour, " + str(sweet) + " sweet")

line = sys.stdin.readline().strip().split()

while line != ['0.0', '0']:
	li = []
	d = float(line[0])
	n = int(line[1])
	for _ in range(n):
		li.append(list(map(float, sys.stdin.readline().strip().split())))

	print(sweet_or_sour(d, li))

	line = sys.stdin.readline().strip().split()


