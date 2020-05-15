def Permute(S):
	if(len(S)<=1):
		return S
	elif(len(S)==2):
		return [S,S[::-1]]
	else:
		output=[]
		curr_el=S[0]
		prev_S=Permute(S[1:])
		for ch in prev_S:
			for i in range(len(ch)+1):
				temp_S=''
				k=0
				for j in range(len(ch)+1):
					if(i==j):
						temp_S+=curr_el
					else:
						temp_S+=ch[k]
						k+=1
				output.append(temp_S)
	return output
S=input()
for p in Permute(S):
	print(p)