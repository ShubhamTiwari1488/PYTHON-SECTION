# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 10:03:30 2023

@author: KIIT
"""

num = int(input("Enter a number: "))
base = int(input("Enter the base value: "))

def DecToBase(num,base):
    num_in_base = []
    while (num != 0):
        remainder = (num%base)
        num = int(num/base)
        num_in_base.append(remainder)
    listToString = ''.join([str(elem) for elem in num_in_base[::-1]])
    print(listToString)
        
DecToBase(num,base)
