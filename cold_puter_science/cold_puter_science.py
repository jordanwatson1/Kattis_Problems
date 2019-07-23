#!/usr/bin/env python3

"""
Kattis: 
July 23, 2019
"""

import sys

n = sys.stdin.readline().strip()

days_neg = [0 if int(i) >= 0 else 1 for i in sys.stdin.readline().strip().split()]

print (sum(days_neg))
