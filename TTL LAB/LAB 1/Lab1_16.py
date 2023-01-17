# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:10:30 2023

@author: KIIT
"""

ch = input("Enter a character ")

if(ch.isdigit()):
    string = "Digit"
    
elif(ch.isalpha()):
    string = "Letter"
    
else:
    string = "Special Character"
    
print("The character entered through keyboard is",string)

    
    