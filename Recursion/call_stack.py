def printer(num):
	if(num<=1):
		print(num)
	else:
		print(num)
		printer(num-1)
printer(6)