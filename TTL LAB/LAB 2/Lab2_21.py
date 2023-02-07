# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:39:33 2023

@author: KIIT
"""

def factorial(n):
 if (n == 0) or (n == 1):
  return 1
 else:
  return (n*factorial(n-1))
 
def calCombination(n, r):
 return int(factorial(n)/(factorial(n-r)*factorial(r)))
 
n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
 for j in range(1, n-i+1):
  print(" ", end="")
 for k in range(1, i+1):
  temp = calCombination(i-1, k-1)
  print(f"{temp} ", end="")
 print('\r')