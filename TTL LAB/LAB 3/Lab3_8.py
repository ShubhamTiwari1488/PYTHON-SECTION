# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 09:58:45 2023

@author: KIIT
"""

n = int(input("Enter the number of rows: "))

def PrintPattern(n):
    for i in range(1, n+1):
        ch = 'A'
        for j in range(i, 0, -1):
            ch = chr(ord(ch)+j-1) # ord() returns the ASCII value for that character
            print(f"{ch} ", end="")
            ch = 'A'
        print('\r')
        
        
PrintPattern(n)