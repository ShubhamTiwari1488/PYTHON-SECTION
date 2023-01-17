# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:33:09 2023

@author: KIIT
"""
import math

a = int(input("Enter the coefficient of x^2 "))
b = int(input("Enter the coefficint of x "))
c = int(input("Enter the constant "))

D = (b*b) - (4*a*c)

if(D>0):
    root = math.sqrt(D)/(2*a)
    
    print("The roots are : ",root," and",-root)
    

elif(D==0):
    root = math.sqrt(D)/(2*a)
    
    print("The root is :",root)
    
else:
    print("The root is imaginary")
    