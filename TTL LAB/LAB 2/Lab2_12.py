# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 09:53:33 2023

@author: KIIT
"""

a = 1
result = 1
sequence = [1]
n = int(input("Enter the number of terms: "))
while n:
 result = ((a*2) + 1)
 a = result
 sequence.append(result)
 n -= 1
print(*sequence)