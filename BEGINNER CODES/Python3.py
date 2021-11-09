
# LEARNING SOME OF THE BASICS OF THE PYTHON3

first=10
second=20

print('\nHere first and second are in int form',first+second)

first="10"
second='20'

print("Here first and second are in string format ",first+second)


# Printing the string a number of times

first="Test"

second=4

print('Printing the string "Test" 4 number of times (there will no spaces )',first*second,end="\n\n\n")

a=input("Enter the value of a ")

b=input("Enter the value of b ")

# If you write 'print(a+b)' it will give you INVALID or may be undesired value as the variables a and b are basically 
# in string objects and they need converted into integer or decimal format before being added together.

print("\nAdding a and b together ",int(a)+(int)(b))	# This will give you correct output as we have converted them to int format


string=input("\nEnter a string ")

num=(int)(input("\nEnter the number of times the string to be printed "))

print("\nOutput ",string*num)

# You can also write it as print("\nOutput ",str(string)*num)  

print(end="\n\n")


