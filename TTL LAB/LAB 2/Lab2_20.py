# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:27:43 2023

@author: KIIT
"""

n = int(input("Enter the number of rows: "))
m = 0

for i in range(n, 0, -1):
    
 for l in range(0, m*2):
     
  print(" ", end="")
  
 for j in range(1, i+1):
     
  print(f'{j} ', end="")
  
 for k in range(i-1, 0, -1):
     
   print(f'{k} ', end="")
  
 m += 1
 
 print('\r')