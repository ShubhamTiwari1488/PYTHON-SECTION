# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 09:21:50 2023

@author: KIIT
"""

a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))

def GCD(a,b):
    if(a%b == 0):
        return b
    
    return GCD(b,a%b)


ans = 0

if(a>b):
    ans = GCD(a,b)
    
else:
    ans = GCD(b,a)

print("The GCD of the two numbers is :",ans)