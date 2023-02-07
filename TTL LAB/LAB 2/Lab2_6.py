# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 09:31:30 2023

@author: KIIT
"""

num = int(input("Enter the range : "))

print("Printing the Even Numbers : ")

for itr in range(1,num+1):
    if(itr%2 == 0):
        print(itr)
        
        
print("Printing the Odd Numbers : ")

for itr in range(1,num+1):
    if(itr%2 != 0):
        print(itr)
        