# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:50:46 2023

@author: KIIT
"""

def getOctal(bit_group):
 return ((4*int(bit_group[0])) + (2*int(bit_group[1])) + (1*int(bit_group[2])))

def getHexadecimal(bit_group):
 n = ((8*int(bit_group[0])) + (4*int(bit_group[1])) + (2*int(bit_group[2])) + (1*int(bit_group[3])))
 if (n > 9):
  ch = 'A'
  return chr(ord(ch)+(n-10))
 else:
  return chr(n)
 
num = input("Enter the binary number: ")
n = len(num)
temp_num = num
while(n%3 != 0):
 num = '0' + num
 n = len(num)
octal = ""
for i in range(0, n, 3):
 octal += str(getOctal(num[i:i+3]))
print(f"{temp_num} in octal: {octal}")
num = temp_num
while (n%4 != 0):
 num = '0' + num
 n = len(num)
hexadecimal = ""
for i in range(0, n, 4):
 hexadecimal += getHexadecimal(num[i:i+4])
print(f"{temp_num} in hexadecimal: {hexadecimal}")