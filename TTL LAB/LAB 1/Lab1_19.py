# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:40:54 2023

@author: KIIT
"""
import math

x1 = float(input("Enter x1 "))
x2 = float(input("Enter x2 "))

y1 = float(input("Enter y1 "))
y2 = float(input("Enter y2 "))


Dis = pow(y2-y1,2) + pow(x2-x1,2)

Dis = math.sqrt(Dis)

print("The Distance between the coordinates are : ",Dis)
