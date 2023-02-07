# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 09:10:53 2023

@author: KIIT
"""

num = int(input("Enter a number : "))

total = 0

while(num != 0):
    #rem = (int)(num%10)
    
    rem = num%10
    
    #print("Rem is ",rem)
    
    total +=rem
    
    num = num//10
    
print("The Sum of digits of the given number :",total)