# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 09:44:16 2023

@author: KIIT
"""

def SumDigit():
    num = int(input("Enter a number : "))

    total = 0

    while(num != 0):
    #rem = (int)(num%10)
    
        rem = num%10
    
    #print("Rem is ",rem)
    
        total +=rem
    
        num = num//10

    return total

print("The Sum of digits of the given number :",SumDigit())