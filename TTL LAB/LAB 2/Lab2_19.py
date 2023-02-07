# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:23:07 2023

@author: KIIT
"""

n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
 if (i%2 != 0):
  for j in range(1, i+1):
   print(f"{j} ", end="")
 else:
  for k in range(i, 0, -1):
   print(f"{k} ", end="")
 print('\r')