def Permute(L):
	if(len(L)<=1):
		return L
	elif(len(L)==2):
		return[L,L[::-1]]
	else:
		output=[]
		curr_El=L[0]
		prev_el=Permute(L[1:])
		
		for el in prev_el:
			for i in range(len(el)+1):
				temp_li=[]
				#temp_el=el.copy()
				k=0
				for j in range(len(el)+1):
					if i==j:
						temp_li.append(curr_El)
					else:
						temp_li.append(el[k])
						k+=1
				output.append(temp_li)
	return output
#print(Permute([1,2,3,4]))
count=0
A=input().split(' ')
B=[]
for a in A:
	B.append(int(a))
for p in Permute(B):
	print(p)
	count+=1
print(count)