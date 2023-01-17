# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:04:13 2023

@author: KIIT
"""

mark = float(input("Enter the marks obtained "))

if(mark <= 100 and mark > 89):
    ch = 'O'
    
elif(mark <=89 and mark > 79):
    ch = 'E'
    
elif(mark <=79 and mark > 69):
    ch = 'A'
    
elif(mark <=69 and mark > 59):
    ch = 'B'
    
elif(mark <=59 and mark > 49):
    ch = 'C'
    
elif(mark <=49 and mark > 39):
    ch = 'D'
    
else:
    ch = 'F'
    
print("The Grade obtained is : ",ch)