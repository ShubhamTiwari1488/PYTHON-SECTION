# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 09:55:47 2023

@author: KIIT
"""

n = int(input("Enter the number of rows: "))

def PrintPattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            if ((i+j)%2 == 0):
                print("1 ", end="")
            else:
                print("0 ", end="")
  
        print('\r')
    
PrintPattern(n)