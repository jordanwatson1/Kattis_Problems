#!/usr/bin/env python3

"""
Kattis: Encoded Message
July 24, 2019
"""

import sys
import math

tests = int(sys.stdin.readline().strip())

for test in range(tests):
	message = sys.stdin.readline().strip()
	row_len = int(math.sqrt(len(message)))
	line = [list(message[i:i+row_len]) for i in range(0, len(message), row_len)]
	decoded_msg = []
	j = row_len - 1
	while j != -1:
		i = 0
		while i < row_len:
			decoded_msg.append(line[i][j])
			i += 1
		j -= 1

	phrase = ''.join(decoded_msg)
	print(phrase)
