# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:42:52 2023

@author: KIIT
"""

string = "KIITCSIT"
n = len(string)
temp1 = string
temp2 = string[::-1]

for i in range(1, int(n)+1):
 print(temp1[:n-i+1], end="")
 for j in range(1, i):
  print(" ", end="")
 print(temp2[i-1:], end="")
 
 print('\r')
for i in range(1, int(n)):
 print(temp1[:i+1], end="")
 for j in range(n-i, 1,-1):
  print(" ", end="")
 print(temp2[n-i-1:], end="")
 print('\r')