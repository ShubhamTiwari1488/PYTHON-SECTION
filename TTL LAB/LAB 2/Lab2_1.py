# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 09:06:20 2023

@author: KIIT
"""

num = int(input("Enter a number : "))

fact = 1

for itr in range(1,num+1):
    fact = fact*itr

print("The Factorial of the number is :",fact)    