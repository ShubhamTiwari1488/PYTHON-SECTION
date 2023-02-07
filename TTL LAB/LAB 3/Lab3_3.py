# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 09:46:40 2023

@author: KIIT
"""

#Reverse the number
def reverseNum():
    num = (int)(input("Enter a number : "))

    reverse_num = 0

    while(num != 0):
        rem = num%10
        
        reverse_num = reverse_num*10 + rem
        
        num = num//10
    
    return reverse_num

print("The reverse number is :",reverseNum())
