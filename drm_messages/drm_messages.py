#!/usr/bin/env python3

"""
Kattis: DRM Messages
July 23, 2019
"""

import sys

text = sys.stdin.readline().strip()
li1 = []
li2 = []
li_final = []

half_len = len(text)//2
# Divide
first_half = text[:half_len]
last_half = text[half_len:]

# Rotate
value_first = 0
value_last = 0
for letter1, letter2  in zip(first_half, last_half):
	value_first += (ord(letter1) - 65)
	value_last += (ord(letter2) - 65)

for letter1, letter2 in zip(first_half, last_half):
	val1 = (ord(letter1) + value_first - 65) % 26
	val2 = (ord(letter2) + value_last - 65) % 26
	li1.append(chr(val1 + 65))
	li2.append(chr(val2 + 65))
	
first_half = ''.join(li1)
last_half = ''.join(li2)

# Merge
for letter1, letter2 in zip(first_half, last_half):
	val1 = ord(letter1) - 65
	val2 = ord(letter2) - 65
	final_letter = (val1 + val2) % 26
	li_final.append(chr(final_letter + 65))

decrypted_msg = ''.join(li_final)

print(decrypted_msg)

