# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:47:02 2023

@author: KIIT
"""

hh_sum = 0
mm_sum = 0
ss_sum = 0

for inp in range(2):
    hh = int(input("Enter value of hh "))
    mm = int(input("Enter value of mm "))
    ss = int(input("Enter value of ss "))
    
    carry = 0
    
    ss_sum +=ss
    
    if(ss_sum > 60):
        carry = ss//60
        
    mm_sum +=mm+carry
    
    if(mm_sum > 60):
        carry = mm//60
        
    else:
        carry = 0
        
    hh_sum +=hh + carry
    

print("The Output is : ",hh_sum,":",mm_sum,":",ss_sum)
