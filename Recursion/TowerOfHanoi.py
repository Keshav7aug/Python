def ToH(num,S='S',A='A',D='D'):
	if(num==1):
		print(S,D)
	else:
		ToH(num-1,S,D,A);
		print(S,D);
		ToH(num-1,A,S,D);
n=int(input())
ToH(n)