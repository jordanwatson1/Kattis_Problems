#!/usr/bin/env python3

"""
Kattis "Aaah!"
July 8, 2019

Input: The input consists of two lines. The first line is the “aaah” 
Jon Marius is able to say that day. The second line is the “aah” the 
doctor wants to hear. Only lowercase ’a’ and ’h’ will be used in the 
input, and each line will contain between 0 and 999 ’a’s, inclusive, 
followed by a single ’h’.

Output: Output “go” if Jon Marius can go to that doctor, and output 
“no” otherwise.
"""

patient = input()
doctor = input()

patient_len = len(patient)
doc_len = len(doctor)

answer = 'go' if patient_len >= doc_len else 'no'

print(answer)
