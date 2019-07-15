#!/usr/bin/env python3

"""
Kattis: A Different Problem
July 14, 2019
"""
import sys

line = sys.stdin.readline().strip()

while line is not '':
	nums = line.split()
	num1 = int(nums[0])
	num2 = int(nums[1])

	sbtr = abs(num1 - num2)
	print(sbtr)

	try:
		line = sys.stdin.readline().strip()
	except:
		break

