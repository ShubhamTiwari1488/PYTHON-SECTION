# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 10:11:45 2023

@author: KIIT
"""

num1 = float(input("Enter the value of num1 "))
num2 = float(input("Enter the value of num2 "))

option = input("Enter the operation you need to perform ")

output = 0

if(option == "add"):
    output = num1+num2
    
elif(option == "sub"):
    output = num1-num2
    
elif(option == "mul"):
    output = num1*num2
    
elif(option == "div"):
    output = num1//num2
    
print("The result is : ",output)
