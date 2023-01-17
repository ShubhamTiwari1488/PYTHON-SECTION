# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 10:06:20 2023

@author: KIIT
"""

string = input("Enter string ")


if(string.islower()):
    string = string.upper()
    
else:
    string = string.lower()
    
print("Output is : ",string)