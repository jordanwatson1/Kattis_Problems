#!/usr/bin/env python3

"""
Kattis: ABC
July 9, 2019

Input: The first line contains the three positive 
integers A, B and C, not necessarily in that order. 
The three numbers will be less than or equal to 100.
The second line contains three uppercase letters ’A’, 
’B’ and ’C’ (with no spaces between them) representing 
the desired order.

Output: Output A, B and C in the desired order on a 
single line, separated by single spaces.
"""
user = input()
order = input()

def order_num(num, order):
	answer = []
	num.sort()

	d = {'A':num[0], 'B':num[1], 'C':num[2]}

	for letter in order:
		ltr = d[letter]
		answer.append(str(ltr))

	return answer[0] + " " + answer[1] + " " + answer[2]

num = user.split()

for i, nums in enumerate(num):
	num[i] = int(nums)

print(order_num(num, order))

