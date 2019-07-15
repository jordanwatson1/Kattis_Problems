#!/usr/bin/env python3

"""
Kattis: ACM Contest Scoring
July 14, 2019

ACM_Contest_Scoring.py takes the users input and puts
each line into a nest list. The list then goes through and 
determines which problems have been solved which is stored 
in a dictionary as {'problem':'right'}. This information is
passed to the function add_minutes which then goes through 
and adds the according penalty to all the problem attemps that 
were not yet finished and then finally adds the time it took 
to solve each problem.
"""

import sys

def add_minutes(prob_attempts, d):
	min = 0
	problems = list(d.keys())

	for (x, y, z) in prob_attempts:
		if (y in problems):
			# penalty
			if (z == 'wrong'):
				min += 20
			# problem solved
			else:
				min += int(x)

	return min

prob_attempts = []
d = {}

line = sys.stdin.readline().strip().split()

while(line[0] != '-1'):
	prob_attempts.append(line)
	line = sys.stdin.readline().strip().split()

# putting the problem letter (key) and if the team has solved it (value)
# in a dictionary
for (_, x, y) in prob_attempts: 
	if (y == 'right'):
		d[x] = y

problems_solved = len(d.items())
total_minutes = add_minutes(prob_attempts, d)

print(str(problems_solved) + ' ' + str(total_minutes))
