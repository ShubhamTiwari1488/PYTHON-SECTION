
# FOR ERROR HANDLING WE HAVE    
#	try: ,except:  

temp=input("\nEnter the fahrenheit Reading ")

try:
	fahr=(float)(temp)
	
	cel=(fahr-32)*5.00/9.00
	
	print("\nThe Celsius Reading is ",round(cel,2))
	
except :
	
	print("\nPlease enter a number",end="\n\n")

