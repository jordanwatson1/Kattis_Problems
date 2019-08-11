#!/usr/bin/env python3

"""
Kattis: Autori
August 11, 2019

Description: Take the first char from each word and join them together.
"""

import sys

names = sys.stdin.readline().strip().split("-")
first_char = [name[0] for name in names]
short_variation = ''.join(first_char)
print(short_variation)
