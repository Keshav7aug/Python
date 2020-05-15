def Palindrome(s):
	if len(s)<=1:
		return 1
	else:
		if s[0]==s[len(s)-1]:
			return Palindrome(s[1:len(s)-1])
		else:
			return 0
S=input()
ans=[" is NOT a"," is a"]
print(S+ans[Palindrome(S)]+" palindrome.")