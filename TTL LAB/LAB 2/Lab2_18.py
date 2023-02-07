# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:18:56 2023

@author: KIIT
"""

n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
 ch = 'A'
 for j in range(i, 0, -1):
  ch = chr(ord(ch)+j-1) # ord() returns the ASCII value for that character
  print(f"{ch} ", end="")
  ch = 'A'
 print('\r')