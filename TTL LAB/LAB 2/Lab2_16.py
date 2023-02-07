# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:11:07 2023

@author: KIIT
"""

n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
 for j in range(1, n-i+1):
  print(" ", end="")
 for k in range(1, i+1):
  print("* ", end="")
 print('\r')