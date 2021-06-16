# TAKE INPUT FROM THE USER AND DISPLAY THE RESULT IN A SORTED MANNER.
# cook your dish here

num=[]

n=int(input())

while(n>0):
    num.append(int(input()))
    n=n-1;
    
num.sort()

for i in num:
    print(i)
    
    
