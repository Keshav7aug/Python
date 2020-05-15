def Staircase(n):
	if(n==0):
		return 1
	elif(n<0):
		return 0
	else:
		return Staircase(n-1)+Staircase(n-2)+Staircase(n-3)
num=int(input())
print(Staircase(num))