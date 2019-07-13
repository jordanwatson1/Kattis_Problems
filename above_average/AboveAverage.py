#!/usr/bin/env python3

"""
Kattis: Above Average
July 12, 2019
"""

import sys

def get_average(num_students, student_grades):
	"""Calculating the average grade of each test case"""
	ave = []

	for num, grades in zip(num_students, student_grades):
		total = sum(grades)

		#avoid division by 0
		if num != 0:
			percent = total / float(num)
			ave.append(percent)
		else:
			ave.append(0)

	return(ave)
		
def above_ave(average, student_grades):
	"""Calculating the percent of students whos final grade is 
	higher than the average"""
	percent_above = []

	for ave, grades in zip(average, student_grades):
		count = 0
		for n, grade in enumerate(grades, start=1):
			if grade > ave:
				count += 1

		#avoid division by 0
		if count != 0:
			percent_above.append((count / float(n)) * 100)
		else:
			percent_above.append(0)

	return percent_above

num_cases = int(sys.stdin.readline().strip())
num_students = []
student_grades = []

for _ in range(num_cases):
	data = sys.stdin.readline().strip().split(' ')
	num_students.append(int(data[0]))
	li = []
	for grade in data[1:]:
		li.append(int(grade))

	student_grades.append(li)

average = get_average(num_students, student_grades)
answer = above_ave(average, student_grades)

for prcnt in answer:
	print("%.3f" % prcnt + '%')



