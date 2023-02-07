# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 09:37:38 2023

@author: KIIT
"""

#Find whether Perfect Number or Not

n = int(input("Enter a number: "))
sum = 0
for i in range(1, int(n/2)+1):
    if (n%i == 0):
        sum += i

if (sum == n):
 print("The given number is a perfect number.")
else:
 print("The given number is not a perfect number.")