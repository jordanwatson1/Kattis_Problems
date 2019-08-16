#!/usr/bin/env python3

"""
Kattis: Pet
August 16, 2019

Description: Determine which contestant received the most points for cooking the best dinner
"""

import sys

top_score = [0, 0]
for i in range(1, 6):
    contestant = list(map(int, sys.stdin.readline().strip().split()))
    score = sum(contestant)
    if score > top_score[0]:
        top_score[0] = score
        top_score[1] = i

print("%d %d" % (top_score[1], top_score[0]))
