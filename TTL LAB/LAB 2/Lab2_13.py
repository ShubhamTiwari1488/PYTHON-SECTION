# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 10:28:07 2023

@author: KIIT
"""

import math
def checkPrime(n):
 for i in range(2, int(math.sqrt(n))+1):
  if (n%i == 0):
      return False
 return True

a = 3
sequence = []
n = int(input("Enter the number of terms: "))

while n>0:
 if (checkPrime(a)):
     sequence.append(a)
     n -= 1
 a += 1
 
print(*sequence)