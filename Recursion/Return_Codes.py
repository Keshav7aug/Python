def NtA(num):
	return chr(num+96)
def Return_Codes(num):
	n=str(num)
	Ans=''
	if(len(n)==1):
		Ans+=append(NtA[num])
	elif(len(n)==2):
		Ans+=NtA(int(n[0]))+NtA(int(n[1]))
		if(num<=26):
			Ans+='\n'+NtA(num)
	else:
		Ans+=NtA(int(n[0]))
		Ans+=Return_Codes(int(n[1:]))
		Ans+='\n'+Return_Codes(int(n[:-1]))
		Ans+=NtA(int(n[-1]))
	return Ans;
print(Return_Codes(123))