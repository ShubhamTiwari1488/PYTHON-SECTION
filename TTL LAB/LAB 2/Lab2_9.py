# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 09:50:02 2023

@author: KIIT
"""

#Find Whether strong number or not
def factorial(n):
 if (n == 1):
  return 1
 else:
  return n*factorial(n-1)
n = int(input("Enter a number: "))

temp_n = n
sum = 0
while (n != 0):
 sum += factorial(n%10)
 n = int(n/10)
if (sum == temp_n):
 print("The given number is a strong number")
else:
 print("The given number is not a strong number")