#!/usr/bin/env python3

"""
Kattis: Above Average
July 12, 2019

Input: The first line of standard input contains an integer 1<=C<=50,
the number of test cases. C data sets follow. Each data set begins 
with an integer, N, the number of people in the class (1<=N<=1000). 
N integers follow, separated by spaces or newlines, each giving 
the final grade (an integer between 0 and 100) of a student in the class.

Output: For each case you are to output a line giving the percentage 
of students whose grade is above average, rounded to exactly 3
decimal places.
"""

import sys

def get_average(num_students, student_grades):
	"""Calculating the average grade of each test case"""
	ave = []

	for num, grades in zip(num_students, student_grades):
		total = 0
		for grade in grades:
			total += grade

		#avoid division by 0
		if num != 0:
			percent = total/float(num)
			ave.append(percent) 

	return(ave)
		
def above_ave(average, student_grades):
	"""Calculating the percent of students whos final grade is 
	higher than the average"""
	percent_above = []

	for ave, grades in zip(average, student_grades):
		count = 0
		for num_studs, grade in enumerate(grades, start=1):
			if grade > ave:
				count += 1

		#avoid division by 0
		if count != 0:
			percent_above.append((count/float(num_studs))*100)
		else:
			percent_above.append(0)

	return percent_above

num_cases = int(sys.stdin.readline())
num_students = []
student_grades = []

i = num_cases
while i > 0:
	num_students.append(int(sys.stdin.read(1)))
	student_grades.append(list(map(int, sys.stdin.readline().strip().split())))
	i -= 1

average = get_average(num_students, student_grades)
answer = above_ave(average, student_grades)

for prcnt in answer:
	print("{0:.3f}%".format(prcnt))


