#!/usr/bin/env python3

"""
Kattis: Harshad Numbers
July 29, 2019
"""

import sys

num = int(sys.stdin.readline().strip())
sum_of_num = 0

for i in str(num):
	sum_of_num += int(i)

while (num % sum_of_num) != 0:
	sum_of_num = 0
	num = num + 1
	for i in str(num):
		sum_of_num += int(i)

print(str(num))
