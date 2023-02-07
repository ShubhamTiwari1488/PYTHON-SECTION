# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 09:19:08 2023

@author: KIIT
"""

num = (int)(input("Enter a number : "))

reverse_num = 0

while(num != 0):
    rem = num%10
    
    reverse_num = reverse_num*10 + rem
    
    num = num//10
    
print("The reverse number is :",reverse_num)
        