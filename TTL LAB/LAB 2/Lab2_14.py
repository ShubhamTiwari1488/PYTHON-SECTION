# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 10:28:20 2023

@author: KIIT
"""

n = int(input("Enter the number of terms: "))
sum = 0
for i in range(1, n+1):
 temp_sum = 0
 for k in range(1, i+1):
  temp_sum += k
  sum += temp_sum
  
print(sum)