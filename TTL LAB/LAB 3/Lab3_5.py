# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 09:51:06 2023

@author: KIIT
"""

import math


num = int(input("Enter a number : "))

def isPrimeNum(num):
    flag = True

    for itr in range(2,int(math.sqrt(num))+1):
        if(num%itr == 0):
            flag = False
            break
    

    if(flag == True):
        print("The Number is a prime number")
    
    else:
        print("The Number is not a prime number")
        
        
isPrimeNum(num)
    