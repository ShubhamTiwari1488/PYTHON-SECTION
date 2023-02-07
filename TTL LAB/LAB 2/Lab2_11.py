# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 09:53:23 2023

@author: KIIT
"""

def fibo(n):
    num1 = 0
    num2 = 1
    
    while(n != 0):
        print(num2,end=" ")
        temp = num2
        num2 = num2+num1
        num1 = temp
        
        n = n - 1
        
num = int(input("Enter the number : "))

fibo(num)

