
# Using math in Python3

import math

signal_power=(float)(input("\nEnter the signal power "))

n=(int)(input("Enter the value of n "))

ratio=signal_power/n

decibel=10*math.log10(ratio)

print("\nDecibel value is :",round(decibel,3))


radian=0.7

height=math.sin(radian)

print("\nRadian was 0.7 ....height was calculated as :",height)

print("\nRoot value of 2 is :",round((math.sqrt(2)),4))

print("\nPrinting value of PI :",math.pi,end="\n")

print("\nValue of 3 to the power of 2 is :",pow(3,2))

print("\n")


