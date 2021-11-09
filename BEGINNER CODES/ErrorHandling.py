
# ERROR HANDLING IN PYTHON3

inp=input('\nEnter a number ')
inp2=input('\nEnter another number ')

try :
	num1=float(inp)
	num2=float(inp2)
	
	print("\nDividing the first with second we get ",round(num1/num2,2))
	
except:
	if(float(num2)==0):
		print("\nPlease enter a non zero value for second num\n")

