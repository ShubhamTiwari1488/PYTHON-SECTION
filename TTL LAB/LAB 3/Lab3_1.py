# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 09:38:05 2023

@author: KIIT
"""

def factorial(num):

    fact = 1

    for itr in range(1,num+1):
        fact = fact*itr
        
    return fact
        
num = int(input("Enter a number : "))

print("The Factorial of the number is :",factorial(num)) 