# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:36:15 2023

@author: KIIT
"""

sum = 0

for itr in range(5):
    mark = float(input("Enter mark for sub "))
    sum +=mark
    
avg = sum/5
per = sum/500*100

print("Average = ",avg," Percentage = ",per)