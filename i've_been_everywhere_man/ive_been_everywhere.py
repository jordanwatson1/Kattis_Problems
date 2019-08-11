#!/usr/bin/env python3

"""
Kattis: I've Been Everywhere, Man
August 11, 2019
"""

import sys

num_tests = int(sys.stdin.readline().strip())

for i in range(num_tests):
    li = []
    tests = int(sys.stdin.readline().strip())

    for j in range(tests):
        li.append(sys.stdin.readline().strip())

    no_duplicates = list(set(li))
    print(len(no_duplicates))
    no_duplicates = []
