#!/usr/bin/env python3

import sys

num_cases = int(sys.stdin.readline())
num_students = []
student_grades = []
answer = []

i = num_cases
while i > 0:
	num_students.append(sys.stdin.read(1))
	student_grades.append(list(map(int, sys.stdin.readline().strip().split())))
	i -= 1

for num, grades in zip(num_students, student_grades):
	
	print(num)
	print(grades)



