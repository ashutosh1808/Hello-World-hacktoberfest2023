'''
program to reverse an integer
'''

num=int(input("Enter an integer: "))
if num<0:	print("inv input, try again")
else:
	rev,digit=0,0
	while num>0:
		digit=num%10
		rev=10*rev+digit
		num//=10
	print("reverse: ",rev)