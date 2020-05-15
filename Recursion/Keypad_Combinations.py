def Key_Comb(num):
	dict={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',9:'wxyz'}
	if num/10 < 1:
		return [el for el in dict[num]]
	else:
		a=dict[num%10]
		b=Key_Comb(num//10)
		ans=[]
		for i in b:
			for j in a:
				ans.append(i+j)
	return ans
	
A=int(input())
print(Key_Comb(A)