# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:29:16 2023

@author: KIIT
"""

a = int(input("Enter the first variable "))
b = int(input("Enter the second variable "))

print("Before swapping the values of a and b are : ",a,b,"respectively")
a = a+b

b = a-b;

a = a-b;

print("After swapping the values of a and b are : ",a,b,"respectively")
