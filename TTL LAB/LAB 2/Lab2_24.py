# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:48:26 2023

@author: KIIT
"""

base = int(input("Enter the base value: "))
num = input(f"Enter the number with base {base}: ")
n = 0
val = 0
for i in num[::-1]:
 val += (int(i)*(base**n))
 n += 1
print(val)