#!/usr/bin/env python3

"""
Kattis: Last Factorial Digit
August 12, 2019

Description: For each value of n, print the last digit of n!
"""
import sys, math

num_test_cases = int(sys.stdin.readline().strip())

for i in range(num_test_cases):
    num = int(sys.stdin.readline().strip())
    num_fac = math.factorial(num)
    print(num_fac % 10)
