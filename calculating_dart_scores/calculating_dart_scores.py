#!/usr/bin/env python3

"""
Kattis: Calculating Dart Scores
July 19, 2019
"""

import sys

def main():
	target_score = int(sys.stdin.readline().strip())
	multiple = ("single", "double", "triple")

	# The first 3 for loops represent the three numbers where the player hit
	# The last three for loops represent the section where the dart was thrown
	# (single, double or triple points). It will exhaust every combo possible
	# and if the target score cannot be found, impossible is printed at the end.
	
	# num1
	for a in range(20, 0, -1):
		# num2
		for b in range(20, 0, -1):
			# num3
			for c in range(20, 0, -1):
				# single, double, or triple
				for x in range(3, -1, -1):
					for y in range(3, -1, -1):
						for z in range(3, -1, -1):
							num = ((a * x) + (b * y) + (c * z))
							if (num == target_score):
								if (x > 0):
									print (multiple[x-1] + " " + str(a))
								if (y > 0):
									print (multiple[y-1] + " " + str(b))
								if (z > 0):
									print (multiple[z-1] + " " + str(c))
								return
	print("impossible")

if __name__ == '__main__':
	main()

