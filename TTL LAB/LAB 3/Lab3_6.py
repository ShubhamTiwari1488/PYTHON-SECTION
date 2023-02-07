# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 09:53:14 2023

@author: KIIT
"""

import math
def checkPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if (n%i == 0):
            return False
    return True

n = int(input("Enter a number: "))
for i in range(2, int(n/2)+1):
 if ((n%i == 0) & checkPrime(i)):
  print(i)

