#!/usr/bin/env python3

"""
Kattis: Nasty Hacks
August 14, 2019

Description: Determine if it is worth the company to
advertise or not, or it doesn't matter
"""

import sys

cases = int(sys.stdin.readline().strip())

for case in range(cases):
    r_e_c = tuple(map(int, sys.stdin.readline().strip().split()))
    no_advertise_rev = r_e_c[0]
    advertise_rev_with_cost = r_e_c[1] - r_e_c[2]
    if no_advertise_rev < advertise_rev_with_cost:
        print("advertise")
    elif no_advertise_rev > advertise_rev_with_cost:
        print("do not advertise")
    else:
        print("does not matter")
