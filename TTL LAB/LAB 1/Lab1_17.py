# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:20:30 2023

@author: KIIT
"""

op1 = int(input("Enter operand 1 : "))
op2 = int(input("Enter operand 2 : "))

op = input("Enter the operator : ")

if(op == "+"):
    ans = op1+op2
    
elif(op == "-"):
    ans = abs(op1-op2)
    
elif(op == "*"):
    ans = op1*op2
    
elif(op == "/"):
    ans = op1/op2
    
print("The result is : ",ans)
