#!/usr/bin/env python3

import sys


num_cases = int(sys.stdin.readline())
num_students = []
student_grades = []

while num_cases > 0:
	num_students.append(sys.stdin.read(1))
	num_cases -= 1

print(num_students)
 


